from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rooms.models import Room
from schools.models import School


class SchoolRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = School.objects.filter(
            slug=self.context['request'].resolver_match.kwargs.get('slug'))
        return queryset


class RoomSerializer(serializers.ModelSerializer):
    school = SchoolRelatedField()
    school_slug = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()
    pupils_count = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=Room.objects.all(),
                fields=['name', 'school'],
                message='There is already a room with this name in this school'
            )
        ]

    def get_school_slug(self, instance):
        return instance.school.slug

    def get_teachers(self, instance):
        return [
            {'id': teacher.id,
             'name': teacher.first_name+' '+teacher.last_name}
            for teacher in instance.teachers.all()]

    def get_pupils_count(self, instance):
        return instance.pupils.count()
