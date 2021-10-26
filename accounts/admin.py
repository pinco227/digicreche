from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import DigiCrecheUser


class DigiCrecheUserAdmin(UserAdmin):
    """Define admin model for custom User model with no email field."""

    model = DigiCrecheUser
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'phone_number',
                       'street_address1', 'street_address2', 'town_or_city',
                       'county', 'postcode', 'country', 'school', 'room')}),
        (_('Billing'), {
            'fields': ('customer',)}),
        (_('Permissions'), {
            'fields': ('user_type', 'is_active', 'is_staff', 'is_superuser',
                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff',
                       'is_active', 'user_type'),
        }),
    )
    list_display = ('id', 'email', 'first_name',
                    'last_name', 'user_type', 'school')
    list_filter = ('email', 'first_name', 'last_name', 'user_type')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(DigiCrecheUser, DigiCrecheUserAdmin)
