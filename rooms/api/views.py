from core.api.permissions import SubscriptionPaidOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rooms.api.permissions import (IsSchoolManager,
                                   IsSchoolManagerOrTeacherParentReadOnly)
from rooms.api.serializers import RoomSerializer
from rooms.models import Room
from schools.models import School


class RoomListCreateAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsSchoolManager, SubscriptionPaidOrReadOnly]

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
    permission_classes = [
        IsSchoolManagerOrTeacherParentReadOnly, SubscriptionPaidOrReadOnly]


class RemoveTeacher(APIView):
    permission_classes = [IsSchoolManager, SubscriptionPaidOrReadOnly]

    def delete(self, request, *args, **kwargs):
        try:
            kwarg_id = self.kwargs.get('id')
            teacher = get_object_or_404(get_user_model(), id=kwarg_id)
            room = teacher.room
            teacher.remove_from_room()
            return Response(
                {
                    'detail': f'{teacher.first_name} {teacher.last_name} '
                    f' was successfully removed from room {room}',
                }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'detail': 'Error! Bad request!',
            }, status=status.HTTP_400_BAD_REQUEST)


class AssignTeacher(APIView):
    permission_classes = [IsSchoolManager, SubscriptionPaidOrReadOnly]

    def post(self, request, *args, **kwargs):
        teacher_id = request.data.get('id')
        room_id = self.kwargs.get('pk')
        try:
            teacher = get_object_or_404(get_user_model(), id=teacher_id)
            room = get_object_or_404(Room, id=room_id)
            if int(teacher.user_type) == 2:
                teacher.assign_to_room(room)
                return Response(
                    {
                        'detail': f'{teacher.first_name} {teacher.last_name} '
                        f' was successfully assigned to room {room.name}',
                    }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'detail': 'Error! Bad request!',
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                'detail': 'Error! Bad request!',
            }, status=status.HTTP_400_BAD_REQUEST)
