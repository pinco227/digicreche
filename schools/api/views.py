from rest_framework import generics, viewsets
from schools.api.permissions import IsManager, IsManagerOrListOnly
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
