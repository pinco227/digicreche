from accounts.api.serializers import ParentSerializer, TeacherSerializer
from core.api.permissions import IsManager
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from rest_framework import generics, viewsets
from schools.api.permissions import (IsManagerOrListOnly,
                                     IsSchoolManagerOrTeacher)
from schools.api.serializers import SchoolSerializer
from schools.models import School


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    lookup_field = 'slug'
    serializer_class = SchoolSerializer
    permission_classes = [IsManagerOrListOnly]

    def perform_create(self, serializer):
        slug = slugify(self.request.data['name'])
        slugs = School.objects.filter(slug=slug)
        if slugs:
            slug = slug + '-' + str(self.request.user.id)

        serializer.save(manager=self.request.user, slug=slug)


class ManagerSchoolList(generics.ListAPIView):
    serializer_class = SchoolSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        manager = self.request.user.id
        return School.objects.filter(
            manager__id=manager).order_by('name')


class SchoolTeachersList(generics.ListAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsSchoolManagerOrTeacher]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return get_user_model().objects.filter(
            school__slug=kwarg_slug, user_type="2").order_by('first_name')


class SchoolUnassignedTeachersList(generics.ListAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsSchoolManagerOrTeacher]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return get_user_model().objects.filter(
            school__slug=kwarg_slug,
            user_type="2",
            room__isnull=True).order_by('first_name')


class SchoolParentsList(generics.ListAPIView):
    serializer_class = ParentSerializer
    permission_classes = [IsSchoolManagerOrTeacher]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return get_user_model().objects.filter(
            school__slug=kwarg_slug, user_type="3").order_by('first_name')
