from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rooms.api import views as sv

router = DefaultRouter()
router.register(r'rooms', sv.RoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
