from django.urls import path
from rooms.api import views as rv

urlpatterns = [
    path('schools/<slug:slug>/rooms/',
         rv.RoomListCreateAPIView.as_view(),
         name='room-list-create'),

    path('schools/<slug:slug>/rooms/<int:pk>/',
         rv.RoomRUDAPIView.as_view(),
         name='room-detail'),

    #     path('schools/<slug:slug>/rooms/<int:pk>/teacher/',
    #          rv.RoomTeacherRUAPIView.as_view(),
    #          name='teacher-detail'),

]
