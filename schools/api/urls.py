from django.urls import include, path
from rest_framework.routers import DefaultRouter
from schools.api import views as sv

router = DefaultRouter()
router.register(r'schools', sv.SchoolViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
