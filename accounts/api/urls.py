from django.urls import path
from accounts.api.views import CurrentUserAPIView

urlpatterns = [
    path('user/', CurrentUserAPIView.as_view(), name='current-user'),
]
