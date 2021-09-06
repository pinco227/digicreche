from rest_framework import serializers
from rooms.models import Room
from django.contrib.auth import get_user_model


class RoomSerializer(serializers.ModelSerializer):
    school_slug = serializers.SerializerMethodField()
    has_teacher = serializers.SerializerMethodField()
    teacher_name = serializers.SerializerMethodField()
    teacher = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.filter(
            user_type=2, room=None),
        required=False)

    class Meta:
        model = Room
        exclude = ['school']

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


# class RoomTeacherSerializer(serializers.ModelSerializer):
#     teacher_queryset = get_user_model().objects.filter(user_type=2)
#     teacher = serializers.PrimaryKeyRelatedField(
#         queryset=teacher_queryset,
#         required=False)

#     class Meta:
#         model = Room
#         fields = ['teacher']
