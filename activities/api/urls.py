from activities.api import views as av
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'activity_types', av.ActivityTypeViewSet)

urlpatterns = [
    path('schools/<slug:slug>/pupils/<int:pk>/activities/',
         av.ActivityListCreateAPIView.as_view(),
         name='activity-list-create'),

    path('schools/<slug:slug>/activity/<int:pk>/',
         av.ActivityRUDAPIView.as_view(),
         name='activity-detail'),

    path('', include(router.urls)),
]
