from rest_framework import serializers
from accounts.models import DigiCrecheUser
from django_countries.serializer_fields import CountryField


class DigiCrecheUserDisplaySerializer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(
        choices=DigiCrecheUser.USER_TYPE_CHOICES)
    country = CountryField()

    class Meta:
        model = DigiCrecheUser
        fields = '__all__'
