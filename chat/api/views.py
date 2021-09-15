# Django Build in User Model
from chat.api.serializers import MessageSerializer
from chat.models import Message
from rest_framework import generics
from django.db.models import Q


class MessageListAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.user.id
        queryset = Message.objects.filter(
            Q(sender__pk=user) | Q(receiver__pk=user)).order_by('-timestamp')
        return queryset


class MessageReadAPIView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        sender = self.request.user
        serializer.save(sender=sender)

    def get_queryset(self):
        user = self.request.user.id
        receiver = self.kwargs.get('pk')
        queryset = Message.objects.filter(
            Q(sender__pk=user, receiver__pk=receiver) |
            Q(sender__pk=receiver, receiver__pk=user)).order_by('timestamp')
        for message in queryset:
            if message.receiver.id == user and message.is_read is False:
                message.is_read = True
                message.save()
        return queryset
