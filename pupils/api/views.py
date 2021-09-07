from rest_framework import generics
from rest_framework.generics import get_object_or_404
from schools.models import School
from pupils.models import Pupil
from pupils.api.serializers import PupilSerializer


class PupilListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer
    # permission_classes = [IsSchoolManager]

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
    # permission_classes = [IsSchoolManagerRUD]
