from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.auth import get_user_model

from chat.api.serializers import MessageSerializer
from chat.models import Message


# CREDIT:
# https://github.com/aogz/django-vue-websocket-chat
class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        self.group_name = 'chat_' + str(self.scope["user"].id)
        await self.channel_layer.group_add(self.group_name, self.channel_name)

    async def disconnect(self, close_code):
        self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        try:
            message = content["message"]
            sender = self.scope['user']
            receiver = await database_sync_to_async(
                get_user_model().objects.get)(id=content["receiver"])

            message = Message(message=message, sender=sender,
                              receiver=receiver)
            await database_sync_to_async(message.save)()

            data = {
                "type": "chat.message",
                **MessageSerializer(message).data
            }

            await self.channel_layer.group_send(
                'chat_' + str(content["receiver"]), data)
            await self.channel_layer.group_send(
                'chat_' + str(self.scope['user'].id), data)

        except Exception as e:
            await self.send_json({'error': str(e)})

    async def chat_message(self, event):
        await self.send_json(event)
