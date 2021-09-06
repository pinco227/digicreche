from rest_framework import viewsets
from schools.api.permissions import IsManagerOrListOnly
from schools.api.serializers import SchoolSerializer
from schools.models import School


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    lookup_field = 'slug'
    serializer_class = SchoolSerializer
    permission_classes = [IsManagerOrListOnly]

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)
