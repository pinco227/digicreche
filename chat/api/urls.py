from chat.api import views
from django.urls import path

urlpatterns = [
    path('chats/',
         views.ConversationListAPIView.as_view(), name='chat-list'),

    path('chats/<int:pk>/',
         views.MessageReadAPIView.as_view(), name='chat-view'),

    path('contacts/',
         views.ContactListAPIView.as_view(), name='contact-list'),
]
