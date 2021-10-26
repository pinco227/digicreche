from django.urls import include, path
from rest_framework.routers import DefaultRouter
from schools.api import views as sv

router = DefaultRouter()
router.register(r'schools', sv.SchoolViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('my-schools/',
         sv.ManagerSchoolList.as_view(),
         name='manager-schools-list'),

    path('schools/<slug:slug>/teachers/',
         sv.SchoolTeachersList.as_view(),
         name='school-teachers-list'),

    path('schools/<slug:slug>/teachers/unassigned/',
         sv.SchoolUnassignedTeachersList.as_view(),
         name='school-teachers-list'),

    path('schools/<slug:slug>/parents/',
         sv.SchoolParentsList.as_view(),
         name='school-parents-list'),
]
