from rest_framework import serializers
from accounts.models import DigiCrecheUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DigiCrecheUser
        exclude = ['password', 'is_superuser', 'is_staff',
                   'is_active', 'groups', 'user_permissions']
