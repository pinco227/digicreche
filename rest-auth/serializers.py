from accounts.models import DigiCrecheUser
from django.db import transaction
from django.utils.functional import lazy
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from schools.models import School


# CREDIT: https://stackoverflow.com/a/52732608
def get_schools():
    try:
        _schools = [('', 'None')] + \
            list(School.objects.all().values_list('id', 'name'))
    except Exception:
        _schools = list(tuple())
    return _schools


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    user_type = serializers.ChoiceField(
        choices=DigiCrecheUser.USER_TYPE_CHOICES)
    first_name = serializers.CharField(max_length=150, required=True)
    last_name = serializers.CharField(max_length=150, required=True)
    phone_number = PhoneNumberField(allow_null=True, allow_blank=True)
    street_address1 = serializers.CharField(
        max_length=100, allow_null=True, allow_blank=True)
    street_address2 = serializers.CharField(
        max_length=100, allow_null=True, allow_blank=True)
    town_or_city = serializers.CharField(max_length=40, required=True)
    county = serializers.CharField(max_length=80, required=True)
    postcode = serializers.CharField(
        max_length=20, allow_null=True, allow_blank=True)
    country = CountryField()
    school = serializers.ChoiceField(
        choices=lazy(get_schools, tuple)(),
        required=False)

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.user_type = self.validated_data.get('user_type')
        user.first_name = self.validated_data.get('first_name')
        user.last_name = self.validated_data.get('last_name')
        user.phone_number = self.data.get('phone_number')
        user.street_address1 = self.validated_data.get('street_address1')
        user.street_address2 = self.validated_data.get('street_address2')
        user.town_or_city = self.validated_data.get('town_or_city')
        user.county = self.validated_data.get('county')
        user.postcode = self.validated_data.get('postcode')
        user.country = self.validated_data.get('country')
        if self.data.get('school'):
            user.school = School.objects.get(
                pk=self.validated_data.get('school'))
        user.save()
        return user


class CustomLoginSerializer(LoginSerializer):
    username = None


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    country = CountryField()
    school_slug = serializers.SerializerMethodField()
    manager = serializers.SerializerMethodField()

    class Meta:
        model = DigiCrecheUser
        fields = ('pk', 'email', 'user_type', 'school', 'manager',
                  'school_slug', 'room', 'first_name', 'last_name',
                  'phone_number', 'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode', 'country',
                  'last_login', 'date_joined')
        read_only_fields = ('pk', 'email', 'user_type', 'last_login',
                            'date_joined')

    def get_school_slug(self, instance):
        return instance.school.slug if instance.school else None

    def get_manager(self, instance):
        return instance.school.manager.pk if instance.school else None
