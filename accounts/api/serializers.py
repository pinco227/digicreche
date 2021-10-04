from rest_framework import serializers
from accounts.models import DigiCrecheUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DigiCrecheUser
        exclude = ['password', 'is_superuser', 'is_staff',
                   'is_active', 'groups', 'user_permissions']


class TeacherSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = DigiCrecheUser
        exclude = ['password', 'is_superuser', 'is_staff',
                   'is_active', 'groups', 'user_permissions', 'user_type',
                   'school']

    def get_name(self, instance):
        return instance.first_name + ' ' + instance.last_name


class ParentSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = DigiCrecheUser
        exclude = ['password', 'is_superuser', 'is_staff',
                   'is_active', 'groups', 'user_permissions', 'user_type',
                   'school', 'room']

    def get_name(self, instance):
        return instance.first_name + ' ' + instance.last_name
