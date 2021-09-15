from django.urls import path
from chat.api import views

urlpatterns = [
    path('messages/',
         views.MessageListAPIView.as_view(), name='message-list'),

    path('messages/<int:pk>/',
         views.MessageReadAPIView.as_view(), name='message-view'),
]
