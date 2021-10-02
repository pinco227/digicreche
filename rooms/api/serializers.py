from rest_framework import serializers
from rooms.models import Room


class RoomSerializer(serializers.ModelSerializer):
    school_slug = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()
    pupils_count = serializers.SerializerMethodField()

    class Meta:
        model = Room
        exclude = ['school']

    def get_school_slug(self, instance):
        return instance.school.slug

    def get_teachers(self, instance):
        return [
            {'id': teacher.id,
             'name': teacher.first_name+' '+teacher.last_name}
            for teacher in instance.teachers.all()]

    def get_pupils_count(self, instance):
        return instance.pupils.count()
