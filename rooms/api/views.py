from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
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


class RemoveTeacher(APIView):
    permission_classes = [IsSchoolManager]

    def delete(self, request, *args, **kwargs):
        try:
            kwarg_id = self.kwargs.get('id')
            teacher = get_object_or_404(get_user_model(), id=kwarg_id)
            teacher.remove_from_room()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AssignTeacher(APIView):
    permission_classes = [IsSchoolManager]

    def post(self, request, *args, **kwargs):
        teacher_id = request.data.get('id')
        room_id = self.kwargs.get('pk')
        try:
            teacher = get_object_or_404(get_user_model(), id=teacher_id)
            room = get_object_or_404(Room, id=room_id)

            teacher.assign_to_room(room)
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
