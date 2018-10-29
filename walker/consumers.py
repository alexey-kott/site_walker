from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
import json

from walker.common_functions import extract_proxies, save_proxy


class WalkerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        await self.close()

    async def receive(self, text_data=None, bytes_data=None):
        msg = json.loads(text_data)

        print(msg)
        method = msg['method']

        if method == 'save_proxies':
            proxies = await extract_proxies(msg['data'])
            await save_proxy(proxies, msg['user_id'])

        await self.send(text_data=json.dumps({
            'message': ''
        }))
