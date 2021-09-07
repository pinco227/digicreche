from django.urls import path
from rooms.api import views as qv

urlpatterns = [
    path('schools/<slug:slug>/rooms/',
         qv.RoomListAPIView.as_view(),
         name='room-list'),

    path('schools/<slug:slug>/room/',
         qv.RoomCreateAPIView.as_view(),
         name='room-create'),

    path('schools/<slug:slug>/rooms/<int:pk>/',
         qv.RoomRUDAPIView.as_view(),
         name='room-detail'),

    #     path('rooms/<int:pk>/teacher/',
    #          qv.RoomTeacherRUAPIView.as_view(),
    #          name='room-teacher'),
]
