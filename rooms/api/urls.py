from django.urls import path
from rooms.api import views as qv

urlpatterns = [
    path('schools/<slug:slug>/rooms/',
         qv.RoomListCreateAPIView.as_view(),
         name='room-list-create'),

    path('schools/<slug:slug>/rooms/<int:pk>/',
         qv.RoomRUDAPIView.as_view(),
         name='room-detail'),

    path('schools/<slug:slug>/rooms/<int:pk>/teacher/',
         qv.RoomTeacherRUAPIView.as_view(),
         name='teacher-detail'),

]
