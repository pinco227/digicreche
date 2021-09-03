from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rooms.api.serializers import RoomSerializer
from rooms.models import Room


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
