import smtplib
from typing import List

import attr
from aiohttp import ClientSession, BasicAuth
import aiohttp
from django.contrib.auth.models import User

from walker.models import ProxyModel


@attr.s
class Proxy:
    host: str = attr.ib()
    port: int = attr.ib()
    username: str = attr.ib()
    password: str = attr.ib()
    enabled: bool = attr.ib(init=False, default=False)


def send_email(email, user_login='', user_password=''):
    server = smtplib.SMTP('smtp.gmail.com', 465)

    # Next, log in to the server
    server.login("site.walker@bk.ru", "QAZwsx!23")

    # Send the mail
    msg = f"Вы успешно зарегистрировались в нашем сервисе. Ваш логин и пароль: {user_login}:{user_password}"
    server.sendmail("site.walker@bk.ru", email, msg)


async def extract_proxy(line):
    try:
        host, port, username, password = line.split(':')
        return Proxy(host, port, username, password)
    except ValueError:
        return None


async def check_proxy(proxy: Proxy):
    async with ClientSession() as session:
        proxy_auth = BasicAuth(proxy.username, proxy.password)
        async with session.get("http://python.org",
                               proxy=f"http://{proxy.host}:{proxy.port}",
                               proxy_auth=proxy_auth) as resp:
            return resp.status == 200


async def extract_proxies(text):
    lines = text.split('\n')
    proxies = []
    for line in lines:
        proxy = await extract_proxy(line.strip(' '))
        if proxy:
            proxy.enabled = await check_proxy(proxy)
            proxies.append(proxy)

    return proxies


async def save_proxy(proxy_list: List[Proxy], user_id):
    user = User.objects.get(pk=user_id)
    for item in proxy_list:
        proxy = ProxyModel.objects.create(owner=user,
                                          host=item.host,
                                          port=item.port,
                                          username=item.username,
                                          password=item.password,
                                          enabled=item.enabled, )
        proxy.save()
