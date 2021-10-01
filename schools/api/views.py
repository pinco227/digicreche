from accounts.models import DigiCrecheUser
from accounts.api.serializers import UserSerializer
from rest_framework import generics, viewsets
from schools.api.permissions import (IsManager, IsManagerOrListOnly,
                                     IsSchoolManager)
from schools.api.serializers import SchoolSerializer
from schools.models import School


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    lookup_field = 'slug'
    serializer_class = SchoolSerializer
    permission_classes = [IsManagerOrListOnly]

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)


class ManagerSchoolList(generics.ListAPIView):
    serializer_class = SchoolSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        manager = self.request.user.id
        return School.objects.filter(
            manager__id=manager).order_by('name')


class SchoolTeachersList(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsSchoolManager]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return DigiCrecheUser.objects.filter(
            school__slug=kwarg_slug).order_by('first_name')
