from accounts.models import DigiCrecheUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = DigiCrecheUser
        exclude = ['password', 'is_superuser', 'is_staff',
                   'is_active', 'groups', 'user_permissions']

    def get_name(self, instance):
        return instance.first_name + ' ' + instance.last_name


class TeacherSerializer(UserSerializer):

    class Meta:
        model = DigiCrecheUser
        exclude = ['password', 'is_superuser', 'is_staff',
                   'is_active', 'groups', 'user_permissions', 'user_type',
                   'school']


class ParentSerializer(UserSerializer):

    class Meta:
        model = DigiCrecheUser
        exclude = ['password', 'is_superuser', 'is_staff',
                   'is_active', 'groups', 'user_permissions', 'user_type',
                   'school', 'room']


class ChatUsertSerializer(UserSerializer):
    unread = serializers.NullBooleanField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = DigiCrecheUser
        fields = ['id', 'name',  'last_login', 'user_type', 'unread']

    def get_name(self, instance):
        if instance.user_type == 1:
            role = 'Manager'
        elif instance.user_type == 2:
            role = 'Teacher'
        else:
            role = 'Parent'

        return f'{instance.first_name} {instance.last_name} ({role})'
