from rest_framework import serializers
from rooms.models import Room


class RoomSerializer(serializers.ModelSerializer):
    school_slug = serializers.SerializerMethodField()

    class Meta:
        model = Room
        exclude = ['school', 'teacher']

    def get_school_slug(self, instance):
        return instance.school.slug
