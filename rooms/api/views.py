from schools.models import School
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rooms.api.serializers import RoomSerializer
from rooms.models import Room


class RoomCreateAPIView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        kwarg_slug = self.kwargs.get('slug')
        school = get_object_or_404(School, slug=kwarg_slug)

        serializer.save(school=school)


class RoomListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return Room.objects.filter(
            school__slug=kwarg_slug).order_by('name')


class RoomRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
