from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import DigiCrecheUser


class DigiCrecheUserAdmin(UserAdmin):
    model = DigiCrecheUser
    list_display = ['username', 'email', 'is_staff']


admin.site.register(DigiCrecheUser, DigiCrecheUserAdmin)
