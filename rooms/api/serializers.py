from rest_framework import serializers
from rooms.models import Room
from django.contrib.auth import get_user_model


class TeacherRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = get_user_model().objects.filter(
            user_type=2,
            room=None,
            school__slug=self.context['request'].resolver_match.kwargs.get(
                'slug'))
        return queryset


class RoomSerializer(serializers.ModelSerializer):
    school_slug = serializers.SerializerMethodField()
    has_teacher = serializers.SerializerMethodField()
    teacher_name = serializers.SerializerMethodField()
    pupils_count = serializers.SerializerMethodField()

    class Meta:
        model = Room
        exclude = ['school', 'teacher']

    def get_school_slug(self, instance):
        return instance.school.slug

    def get_has_teacher(self, instance):
        return bool(instance.teacher)

    def get_teacher_name(self, instance):
        if instance.teacher:
            return (
                instance.teacher.first_name + ' ' + instance.teacher.last_name)
        else:
            return None

    def get_pupils_count(self, instance):
        return instance.pupils.count()


class RoomTeacherSerializer(serializers.ModelSerializer):
    teacher = TeacherRelatedField()

    class Meta:
        model = Room
        fields = ['teacher']
