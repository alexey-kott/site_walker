import logging
import os
import subprocess
import asyncio
import smtplib
from typing import List, Union, Dict, Tuple, Optional as Opt

from aiohttp import ClientSession, BasicAuth
from django.db import IntegrityError

from walker_panel.models import Proxy

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='./logs/log')
logger = logging.getLogger('site_walker')
logger.setLevel(logging.ERROR)


def send_email(email, user_login='', user_password=''):
    server = smtplib.SMTP('smtp.mail.ru', 465)

    # Next, log in to the server
    server.login("site.walker@bk.ru", "QAZwsx!23")

    # Send the mail
    msg = f"Вы успешно зарегистрировались в нашем сервисе. Ваш логин и пароль: {user_login}:{user_password}"
    server.sendmail("site.walker@bk.ru", email, msg)


def extract_proxy(line: str) -> Tuple[str, str, Opt[str], Opt[str]]:
    try:
        if len(line.split(':')) == 2:
            host, port = line.split(':')
            username = password = None
        elif len(line.split(':')) == 4:
            host, port, username, password = line.split(':')
        else:
            logger.error(f'Proxy line parsing failed: {line}')
            return

        return host, port, username, password
    except ValueError as e:
        logger.error(f'Proxy line parsing failed: {line}. Exception message: {e}')


async def check_proxy_enable(host: str, port:str, username: str, password: str) -> Dict[str, Union[str, bool]]:
    async with ClientSession() as session:
        if username is None:
            proxy_auth = None
        else:
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
            host, port, username, password = extract_proxy(line.strip(' \n\r'))
            coroutines.append(check_proxy_enable(host, port, username, password))
        except ValueError as e:
            print(e)

    raw_proxies = await asyncio.gather(*coroutines)
    for item in raw_proxies:
        try:
            proxy, was_created = Proxy.objects.get_or_create(owner=user,
                                                             host=item['host'],
                                                             port=item['port'],
                                                             username=item['username'],
                                                             password=item['password'],
                                                             enabled=item['enabled'])
        except IntegrityError as e:
            print(e)
        # proxies.append(proxy)
    #
    # return proxies


def is_service_running(name):
    with open(os.devnull, 'wb') as hide_output:
        exit_code = subprocess.Popen(['service', name, 'status'], stdout=hide_output, stderr=hide_output).wait()
        return exit_code == 0
