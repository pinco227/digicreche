from django.urls import path
from pupils.api import views as qv

urlpatterns = [
    path('schools/<slug:slug>/pupils/',
         qv.PupilListCreateAPIView.as_view(),
         name='pupil-list-create'),

    path('schools/<slug:slug>/pupils/<int:pk>/',
         qv.PupilRUDAPIView.as_view(),
         name='pupil-detail'),

]
