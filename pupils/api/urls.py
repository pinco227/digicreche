from django.urls import path
from pupils.api import views as pv

urlpatterns = [
    path('schools/<slug:slug>/pupils/',
         pv.PupilListCreateAPIView.as_view(),
         name='pupil-list-create'),

    path('schools/<slug:slug>/rooms/<int:pk>/pupils/',
         pv.PupilRoomListAPIView.as_view(),
         name='room-detail'),

    path('schools/<slug:slug>/unassigned/',
         pv.UnassignedListAPIView.as_view(),
         name='unassigned-list'),

    path('schools/<slug:slug>/pupils/<int:pk>/',
         pv.PupilRUDAPIView.as_view(),
         name='pupil-detail'),

    path('children/',
         pv.ChildrenListAPIView.as_view(),
         name='children-list'),

]
