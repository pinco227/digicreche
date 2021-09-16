from rest_framework import serializers
from pupils.models import Pupil
from rooms.models import Room
# from accounts.api.serializers import UserSerializer
from django.contrib.auth import get_user_model


class RoomRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = Room.objects.filter(
            school__slug=self.context['request'].resolver_match.kwargs.get(
                'slug'))
        return queryset


class ParentRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = get_user_model().objects.filter(
            school__slug=self.context['request'].resolver_match.kwargs.get(
                'slug'), user_type=3)
        return queryset


class PupilSerializer(serializers.ModelSerializer):
    room = RoomRelatedField(allow_null=True)
    parents = ParentRelatedField(many=True)

    class Meta:
        model = Pupil
        # exclude = ['school']
        fields = '__all__'
