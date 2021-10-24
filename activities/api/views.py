from activities.api.pagination import PageNumPagination
from activities.api.permissions import (IsAdminOrSafe,
                                        IsSchoolManagerTeacherParentRUD,
                                        IsSchoolManagerTeacherParentSafe)
from activities.api.serializers import (ActivitySerializer,
                                        ActivityTypeSerializer)
from activities.models import Activity, ActivityType
from core.api.permissions import SubscriptionPaidOrReadOnly
from pupils.models import Pupil
from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


class ActivityTypeViewSet(viewsets.ModelViewSet):
    queryset = ActivityType.objects.all().order_by('name')
    serializer_class = ActivityTypeSerializer
    permission_classes = [IsAdminOrSafe]


class ActivityListCreateAPIView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    pagination_class = PageNumPagination
    permission_classes = [
        IsSchoolManagerTeacherParentSafe, SubscriptionPaidOrReadOnly]

    def create(self, request, *args, **kwargs):
        """ CREDIT https://www.py4u.net/discuss/192406"""

        file_fields = list(request.FILES.keys())
        serializer = self.get_serializer(
            data=request.data, file_fields=file_fields)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

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
    permission_classes = [
        IsSchoolManagerTeacherParentRUD, SubscriptionPaidOrReadOnly]
