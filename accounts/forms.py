from django_registration.forms import RegistrationForm
from .models import DigiCrecheUser


class DigiCrecheUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = DigiCrecheUser
