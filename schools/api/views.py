from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from schools.api.permissions import IsManagerOrReadOnly
from schools.api.serializers import SchoolSerializer
from schools.models import School


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    lookup_field = 'slug'
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsManagerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)
