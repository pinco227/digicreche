from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from djstripe.models import Customer
from phonenumber_field.modelfields import PhoneNumberField
from rooms.models import Room
from schools.models import School

from .managers import CustomUserManager


class DigiCrecheUser(AbstractUser):

    USER_TYPE_CHOICES = (
        (1, 'Manager'),
        (2, 'Teacher'),
        (3, 'Parent'),
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    username = None
    email = models.EmailField(
        _('Email Address'), unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )
    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, default='3')
    first_name = models.CharField(
        _('first name'), max_length=150, null=False, blank=False)
    last_name = models.CharField(
        _('last name'), max_length=150, null=False, blank=False)
    phone_number = PhoneNumberField(null=True, blank=True)
    street_address1 = models.CharField(max_length=100, null=True, blank=True)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label="Country ", null=False, blank=False)
    school = models.ForeignKey(
        School, on_delete=models.DO_NOTHING, null=True,
        blank=True, related_name='institution',
        help_text='Leave blank if you are a manager.')
    room = models.ForeignKey(
        Room, null=True, blank=True, on_delete=models.SET_NULL,
        related_name='teachers')
    customer = models.ForeignKey(
        Customer, null=True, blank=True, on_delete=models.SET_NULL,
        help_text="The user's Stripe Customer object, if it exists"
    )

    objects = CustomUserManager()

    def __str__(self):
        return (self.first_name+' '+self.last_name +
                ' ('+self.get_user_type_display()+')')

    def remove_from_room(self):
        self.room = None
        self.save()

    def assign_to_room(self, room):
        self.room = room
        self.save()
