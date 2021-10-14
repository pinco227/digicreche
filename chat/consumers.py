from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from chat.api.serializers import MessageSerializer
from chat.models import Message
from django.contrib.auth import get_user_model as User


class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.group_name = self.scope['user']['email']
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        try:
            message = content["message"]
            sender = self.scope['user']
            receiver = User.objects.filter(pk=content["receiver"]).first()
            message = await database_sync_to_async(
                Message(message=message, sender=sender,
                        receiver=receiver).save())

            data = {
                "type": "chat.message",
                **MessageSerializer(message).data
            }

            await self.channel_layer.group_send(receiver.email, data)

        except Exception as e:
            await self.send_json({'error': str(e)})

    async def chat_message(self, event):
        await self.send_json(event)
