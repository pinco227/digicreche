from accounts.api.serializers import ChatUsertSerializer
from chat.api.pagination import PageNumPagination
from chat.api.serializers import MessageSerializer
from chat.models import Message
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from schools.models import School


class ConversationListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        chats = []
        messages = Message.objects.filter(
            Q(sender__pk=user.id) | Q(receiver__pk=user.id)
        ).order_by('-timestamp')
        for message in messages:
            chat = message.sender if message.sender != user \
                else message.receiver
            new_chat = chat
            new_chat.unread = True if not message.is_read and \
                message.receiver == user else False

            if chat in chats:
                if not message.is_read:
                    chat_index = chats.index(chat)
                    chats[chat_index] = new_chat
            else:
                chats.append(new_chat)

        serializer = ChatUsertSerializer(
            chats, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class MessageReadAPIView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    pagination_class = PageNumPagination

    def perform_create(self, serializer):
        sender = self.request.user
        serializer.save(sender=sender)

    def get_queryset(self):
        user = self.request.user.id
        receiver = self.kwargs.get('pk')
        queryset = Message.objects.filter(
            Q(sender__pk=user, receiver__pk=receiver) |
            Q(sender__pk=receiver, receiver__pk=user)).order_by('-timestamp')
        for message in queryset:
            if message.receiver.id == user and message.is_read is False:
                message.is_read = True
                message.save()
        return queryset


class ContactListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        user = request.user
        user_type = user.user_type

        if user_type == 1:
            schools = School.objects.filter(manager=user)
            queryset = get_user_model().objects.filter(
                school__in=schools).order_by('user_type')
        elif user_type == 2:
            if user.school:
                queryset = get_user_model().objects.filter(
                    Q(id=user.school.manager.id) |
                    (Q(school=user.school) & ~Q(id=user.id))
                ).order_by('user_type')
            else:
                queryset = None
        else:
            if user.school:
                queryset = get_user_model().objects.filter(
                    Q(id=user.school.manager.id) |
                    (Q(school=user.school) & Q(user_type=2))
                ).order_by('user_type')
            else:
                queryset = None

        serializer = ChatUsertSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
