from rest_framework.routers import SimpleRouter
from rooms.api import views as sv

router = SimpleRouter()
router.register(r'rooms', sv.RoomViewSet)
