from django.contrib.auth import get_user_model
from pupils.models import Pupil
from rest_framework import serializers
from rooms.models import Room


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
    school_slug = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Pupil
        fields = '__all__'

    def get_school_slug(self, instance):
        return instance.school.slug

    def get_name(self, instance):
        return instance.first_name + ' ' + instance.last_name


class PupilPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pupil
        fields = ['photo', ]


class PupilDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pupil
        fields = ['personal_details', ]


class PupilRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pupil
        fields = ['room', ]
