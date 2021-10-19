from rest_framework import serializers
from schools.models import School
from accounts.models import DigiCrecheUser


class ManagerRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = DigiCrecheUser.objects.filter(
            id=self.context['request'].user.id)
        return queryset


class SchoolSerializer(serializers.ModelSerializer):
    manager = ManagerRelatedField()
    rooms_count = serializers.SerializerMethodField()
    pupils_count = serializers.SerializerMethodField()
    unassigned_pupils = serializers.SerializerMethodField()
    teachers_count = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()
    subscription = serializers.PrimaryKeyRelatedField(read_only=True)

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

    def validate(self, data):
        """
        Check if email is userd by other managers
        """
        print(" ")
        print(data['manager'])
        print(" ")
        schools = School.objects.filter(
            email=data['email']).exclude(manager=data['manager'])
        print(schools)

        if schools:
            raise serializers.ValidationError(
                {"email": "This email is already used by a different school."})
        return data
