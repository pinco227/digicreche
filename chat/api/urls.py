from django.urls import path
from chat.api import views

urlpatterns = [
    path('messages/<int:pk>/<int:receiver>/',
         views.MessageReadAPIView.as_view(), name='message-detail'),

    path('messages/', views.MessageListCreateAPIView.as_view(),
         name='message-list'),
]
