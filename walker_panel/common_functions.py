import asyncio
import smtplib
from typing import List, Union, Dict

from aiohttp import ClientSession, BasicAuth
from django.db import IntegrityError

from walker_panel.models import Proxy


def send_email(email, user_login='', user_password=''):
    server = smtplib.SMTP('smtp.mail.ru', 465)

    # Next, log in to the server
    server.login("site.walker@bk.ru", "QAZwsx!23")

    # Send the mail
    msg = f"Вы успешно зарегистрировались в нашем сервисе. Ваш логин и пароль: {user_login}:{user_password}"
    server.sendmail("site.walker@bk.ru", email, msg)


def extract_proxy(line):
    try:
        host, port, username, password = line.split(':')
        return host, port, username, password
    except ValueError as e:
        print('Proxy extract error', e)
        return None


async def check_proxy_enable(host: str, port:str, username: str, password: str) -> Dict[str, Union[str, bool]]:
    async with ClientSession() as session:
        proxy_auth = BasicAuth(username, password)
        async with session.get("http://python.org",
                               proxy=f"http://{host}:{port}",
                               proxy_auth=proxy_auth) as resp:
            return {'host': host,
                    'port': port,
                    'username': username,
                    'password': password,
                    'enabled': resp.status == 200}


async def save_proxies(user, text_data) -> List[Proxy]:
    lines = text_data.split('\n')
    proxies = []
    coroutines = []
    for line in lines:
        try:
            host, port, username, password = extract_proxy(line.strip(' \n'))
            coroutines.append(check_proxy_enable(host, port, username, password))
        except ValueError as e:
            print(e)

    result = await asyncio.gather(*coroutines)

    for item in result:
        try:
            proxy, was_created = Proxy.objects.get_or_create(owner=user,
                                                             host=item['host'],
                                                             port=item['port'],
                                                             username=item['username'],
                                                             password=item['password'],
                                                             enabled=item['enabled'])
        except IntegrityError as e:
            print(e)
        proxies.append(proxy)


    return proxies
