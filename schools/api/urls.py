from django.urls import path, include
from rest_framework.routers import DefaultRouter
from schools.api import views as sv

router = DefaultRouter()
router.register(r'schools', sv.SchoolViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('my-schools/',
         sv.ManagerSchoolList.as_view(),
         name='manager-schools-list'),
]
