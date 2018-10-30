import smtplib
from typing import List

import attr
from aiohttp import ClientSession, BasicAuth
import aiohttp
from django.contrib.auth.models import User

from walker.models import Proxy


# @attr.s
# class Proxy:
#     host: str = attr.ib()
#     port: int = attr.ib()
#     username: str = attr.ib()
#     password: str = attr.ib()
#     enabled: bool = attr.ib(init=False, default=False)


def send_email(email, user_login='', user_password=''):
    server = smtplib.SMTP('smtp.gmail.com', 465)

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


async def check_proxy_enable(host, port, username, password):
    async with ClientSession() as session:
        proxy_auth = BasicAuth(username, password)
        async with session.get("http://python.org",
                               proxy=f"http://{host}:{port}",
                               proxy_auth=proxy_auth) as resp:
            return resp.status == 200


async def save_proxies(user, text_data) -> List[Proxy]:
    lines = text_data.split('\n')
    proxies = []
    for line in lines:
        print(line)
        try:
            host, port, username, password = extract_proxy(line.strip(' '))
            enabled = await check_proxy_enable(host, port, username, password)

            proxy, was_created = Proxy.objects.get_or_create(owner=user,
                                                             host=host,
                                                             port=port,
                                                             username=username,
                                                             password=password,
                                                             enabled=enabled)
            if was_created:
                proxy.save()
            proxies.append(proxy)
        except ValueError as e:
            print(e)

    return proxies
