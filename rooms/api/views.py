from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rooms.api.permissions import (IsSchoolManager,
                                   IsSchoolManagerOrTeacherReadOnly)
from rooms.api.serializers import RoomSerializer
from rooms.models import Room
from schools.models import School


class RoomListCreateAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsSchoolManager]

    def perform_create(self, serializer):
        kwarg_slug = self.kwargs.get('slug')
        school = get_object_or_404(School, slug=kwarg_slug)

        serializer.save(school=school)

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return Room.objects.filter(
            school__slug=kwarg_slug).order_by('name')


class RoomRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsSchoolManagerOrTeacherReadOnly]


# class RoomTeacherRUAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomTeacherSerializer
#     permission_classes = [IsSchoolManagerOrTeacherReadOnly]

#     def delete(self, request, *args, **kwargs):
#         room = self.get_object()
#         room.remove_teacher()
#         return Response(status=status.HTTP_204_NO_CONTENT)
