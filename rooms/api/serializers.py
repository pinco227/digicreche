from rest_framework import serializers
from rooms.models import Room
# from django.contrib.auth import get_user_model


# class TeacherRelatedField(serializers.PrimaryKeyRelatedField):
#     def get_queryset(self):
#         queryset = get_user_model().objects.filter(
#             user_type=2,
#             room=None,
#             school__slug=self.context['request'].resolver_match.kwargs.get(
#                 'slug'))
#         return queryset


class RoomSerializer(serializers.ModelSerializer):
    school_slug = serializers.SerializerMethodField()
    has_teacher = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()
    pupils_count = serializers.SerializerMethodField()

    class Meta:
        model = Room
        exclude = ['school']

    def get_school_slug(self, instance):
        return instance.school.slug

    def get_has_teacher(self, instance):
        return bool(instance.teachers)

    def get_teachers(self, instance):
        return [
            {'id': teacher.id, 'name': teacher.first_name+' '+teacher.last_name}
            for teacher in instance.teachers.all()]

    def get_pupils_count(self, instance):
        return instance.pupils.count()


# class RoomTeacherSerializer(serializers.ModelSerializer):
#     teacher = TeacherRelatedField()

#     class Meta:
#         model = Room
#         fields = ['teacher']
