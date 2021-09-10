from django.contrib import admin
from .models import Activity, ActivityType, ActivityImage

# CREDIT:
# https://soshace.com/upload-multiple-images-to-a-django-model-without-plugins/


class ActivityImageAdmin(admin.StackedInline):
    model = ActivityImage


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    inlines = [ActivityImageAdmin]
    model = Activity


@admin.register(ActivityImage)
class ActivityImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(ActivityType)
