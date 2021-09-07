from rest_framework import serializers
from pupils.models import Pupil


class PupilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pupil
        exclude = ['school']
