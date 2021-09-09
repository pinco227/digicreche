from django.contrib import admin
from .models import Activity, ActivityType, ActivityImage


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
