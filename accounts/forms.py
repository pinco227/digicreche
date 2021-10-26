from django import forms
from django_registration.forms import RegistrationForm

from .models import DigiCrecheUser


class DigiCrecheUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = DigiCrecheUser
        widgets = {
            'user_type': forms.RadioSelect,
        }
        fields = ['user_type', 'email', 'first_name', 'last_name',
                  'phone_number', 'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode', 'country', 'school']
