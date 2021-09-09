from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from activities.api.serializers import (ActivitySerializer,
                                        ActivityTypeSerializer)
from activities.models import Activity, ActivityType
from pupils.models import Pupil
from activities.api.permissions import (IsSchoolManagerTeacherParentSafe,
                                        IsSchoolManagerTeacherParentRUD)


class ActivityTypeViewSet(viewsets.ModelViewSet):
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer
    permission_classes = [IsAdminUser]


class ActivityListCreateAPIView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsSchoolManagerTeacherParentSafe]

    def perform_create(self, serializer):
        kwarg_pk = self.kwargs.get('pk')
        pupil = get_object_or_404(Pupil, pk=kwarg_pk)

        serializer.save(pupil=pupil)

    def get_queryset(self):
        kwarg_pk = self.kwargs.get('pk')
        return Activity.objects.filter(
            pupil__pk=kwarg_pk).order_by('-created_at')


class ActivityRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsSchoolManagerTeacherParentRUD]
