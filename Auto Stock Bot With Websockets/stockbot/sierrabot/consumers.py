from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
import time, json, random, asyncio
import websocket
from asgiref.sync import async_to_sync, sync_to_async
import channels

'''
class StockData(WebsocketConsumer):
    def connect(self):
        self.group_name = "stockdata"
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def receive(self, text_data):
        print(" MESSAGE RECEIVED From FrontEnd")
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, {"type": "someRandomFunction", "value": text_data,}
        )

    def disconnect(self, close_code):
        self.close()

    def someRandomFunction(self, event):
        print(event["value"])

        def on_open(ws):
            print("opened")
            auth_data = {
                "action": "authenticate",
                "data": {
                    "key_id": "PK0FQRLC49D83ZE804WW",
                    "secret_key": "5edRjGfh0ubqqvztzTOZbTRzu39QPqmzJb2NLQaF",
                },
            }
            ws.send(json.dumps(auth_data))
            listen_message = {
                "action": "listen",
                "data": {"streams": ["T.AAPL", "T.MSFT", "T.TSLA"]},
            }
            ws.send(json.dumps(listen_message))

        def on_message(ws, message):
            print("received a message")
            print(message)
            channel_layer = channels.layers.get_channel_layer()
            channel_layer.send(
                channel_layer.group_name,
                json.dumps({"type": "websocket.send", "text": message,}),
            )
            # channel_layer.send(json.dumps({"type": "websocket.send", "text": message,}))
            sync_to_async(channel_layer.group_send)(
                channel_layer.group_name,
                json.dumps({"type": "websocket.send", "text": message,}),
            )
            # sync_to_async(
            #     (self.channel_layer.send)({"type": "websocket.send", "text": message,}),
            # )

        def on_close(ws):
            print("closed connection")
            ws.close()

        print("Before Scoket Creation")
        socket = "wss://data.alpaca.markets/stream"
        ws = websocket.WebSocketApp(
            socket, on_open=on_open, on_message=on_message, on_close=on_close,
        )
        # print(ws)
        ws.run_forever()
        # await asyncio.get_running_loop().run_in_executor()


'''
class StockData(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "stockdata"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data):

        await self.channel_layer.group_send(
            self.group_name, {"type": "someRandomFunction", "value": text_data,}
        )

    async def disconnect(self, close_code):
        await self.close()

    async def someRandomFunction(self, event):
        print(event["value"])

        def on_open(ws):
            print("opened")
            auth_data = {
                "action": "authenticate",
                "data": {
                    "key_id": "PK0FQRLC49D83ZE804WW",
                    "secret_key": "5edRjGfh0ubqqvztzTOZbTRzu39QPqmzJb2NLQaF",
                },
            }
            ws.send(json.dumps(auth_data))
            listen_message = {
                "action": "listen",
                "data": {"streams": ["T.AAPL", "T.MSFT", "T.TSLA"]},
            }
            ws.send(json.dumps(listen_message))

        def on_message(ws, message):
            print("received a message")
            print(message)
            channel_layer = channels.layers.get_channel_layer()

            # channel_layer.send(json.dumps({"type": "websocket.send", "text": message,}))
            sync_to_async(
                channel_layer.group_send(
                    json.dumps({"type": "websocket.send", "text": message,})
                )
            )
            # sync_to_async(
            #     (self.channel_layer.send)({"type": "websocket.send", "text": message,}),
            # )

        def on_close(ws):
            print("closed connection")

        print("Before Scoket Creation")
        socket = "wss://data.alpaca.markets/stream"
        ws = websocket.WebSocketApp(
            socket, on_open=on_open, on_message=on_message, on_close=on_close,
        )
        print(ws)
        ws.run_forever()
        # await asyncio.get_running_loop().run_in_executor()

        """
        while True:
            await asyncio.sleep(1)
            listOfindex = ["stock1", "stock2", "stock3", "stock4", "stock5"]
            obj = {
                "indexName": random.choice(listOfindex),
                "value": random.randint(1, 1000),
            }

            await self.send(json.dumps({"type": "websocket.send", "text": obj,}))
        """
        # await self.send(event["value"])

