from channels.generic.websocket import AsyncWebsocketConsumer

class ReadConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        Connect a client to the websocket.
        Specific actions to be performed when a client gets connected is also defined here.
        """
        await self.accept()
    
    async def disconnect(self, code):
        """
        Actions to be performed when a client disconnects
        """
        pass

    async def receive(self, text_data=None, bytes_data=None):
        """
        Actions to be performed when websocket receives data from a client
        """
        print(text_data)

"""
To send data from websocket use: 
    "await self.send(<message>)" if self.send is being used in async function
    OR
    from asgiref.sync import async_to_sync
    async_to_sync(self.send)(<message>) if self.send is being used in sync function
"""
