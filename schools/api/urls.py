from rest_framework.routers import SimpleRouter
from schools.api import views as sv

router = SimpleRouter()
router.register(r'schools', sv.SchoolViewSet)
