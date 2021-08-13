from django.conf import settings
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class School(models.Model):

    manager = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                blank=False, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True,
                            null=False, blank=False)
    description = models.TextField()
    email = models.EmailField(max_length=255, unique=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    street_address1 = models.CharField(max_length=100, null=True, blank=True)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label="Country ", null=False, blank=False)

    def __str__(self):
        return self.name
