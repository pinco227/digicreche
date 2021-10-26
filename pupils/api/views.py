from core.api.permissions import SubscriptionPaidOrReadOnly
from pupils.api.permissions import (IsSchoolManager,
                                    IsSchoolManagerOrParentRUD,
                                    IsSchoolManagerParentTeacherRUD,
                                    IsSchoolManagerTeacherSafe)
from pupils.api.serializers import (PupilDetailsSerializer,
                                    PupilPhotoSerializer, PupilRoomSerializer,
                                    PupilSerializer)
from pupils.models import Pupil
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from schools.models import School


class UnassignedListAPIView(generics.ListAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer
    permission_classes = [IsSchoolManager]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return Pupil.objects.filter(
            school__slug=kwarg_slug, room=None).order_by('last_name')


class PupilRoomListAPIView(generics.ListAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer
    permission_classes = [IsSchoolManagerTeacherSafe]

    def get_queryset(self):
        school_slug = self.kwargs.get('slug')
        room_id = self.kwargs.get('pk')
        return Pupil.objects.filter(
            school__slug=school_slug, room__pk=room_id).order_by('last_name')


class ChildrenListAPIView(generics.ListAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer

    def get_queryset(self):
        parent = self.request.user.id
        return Pupil.objects.filter(
            parents__id__contains=parent).order_by('first_name')


class PupilListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer
    permission_classes = [
        IsSchoolManager, SubscriptionPaidOrReadOnly]

    def perform_create(self, serializer):
        kwarg_slug = self.kwargs.get('slug')
        school = get_object_or_404(School, slug=kwarg_slug)

        serializer.save(school=school)

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return Pupil.objects.filter(
            school__slug=kwarg_slug).order_by('last_name')


class PupilRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer
    permission_classes = [
        IsSchoolManagerParentTeacherRUD, SubscriptionPaidOrReadOnly]

    def perform_update(self, serializer):
        kwarg_slug = self.kwargs.get('slug')
        school = get_object_or_404(School, slug=kwarg_slug)

        serializer.save(school=school)


class PupilPhotoAPIView(generics.RetrieveUpdateAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilPhotoSerializer
    permission_classes = [
        IsSchoolManagerOrParentRUD, SubscriptionPaidOrReadOnly]


class PupilDetailsAPIView(generics.RetrieveUpdateAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilDetailsSerializer
    permission_classes = [
        IsSchoolManagerOrParentRUD, SubscriptionPaidOrReadOnly]


class PupilRoomAPIView(generics.RetrieveUpdateAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilRoomSerializer
    permission_classes = [
        IsSchoolManagerParentTeacherRUD, SubscriptionPaidOrReadOnly]
