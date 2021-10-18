from rest_framework import serializers
from schools.models import School


class SchoolSerializer(serializers.ModelSerializer):
    manager = serializers.StringRelatedField(read_only=True)
    rooms_count = serializers.SerializerMethodField()
    pupils_count = serializers.SerializerMethodField()
    unassigned_pupils = serializers.SerializerMethodField()
    teachers_count = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = '__all__'

    def get_rooms_count(self, instance):
        return instance.rooms.count()

    def get_pupils_count(self, instance):
        return instance.students.count()

    def get_unassigned_pupils(self, instance):
        return instance.students.filter(room=None).count()

    def get_teachers_count(self, instance):
        return instance.institution.filter(user_type="2").count()

    def get_is_active(self, instance):
        return (instance.subscription is not None and
                instance.subscription.is_valid())
