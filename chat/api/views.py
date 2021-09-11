# Django Build in User Model
from chat.api.serializers import MessageSerializer
from chat.models import Message
from rest_framework import generics


class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageReadAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        sender = self.kwargs.get('pk')
        receiver = self.kwargs.get('receiver')
        return Message.objects.filter(
            sender__id=sender, receiver__id=receiver)
