from channels.generic.websocket import AsyncWebsocketConsumer
import json


class WalkerConsumer(AsyncWebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        self.close()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        # message = text_data_json['message']
        #
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))