from activities.models import Activity
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from schools.models import School


class SubscriptionPaidOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            kwarg_slug = request.parser_context['kwargs']['slug']
            school = get_object_or_404(School, slug=kwarg_slug)
            subscription = school.subscription
        except Exception:
            return False

        return ((subscription is not None and
                 subscription.is_valid()) or
                request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Activity):
            subscription = obj.pupil.school.subscription
        else:
            subscription = obj.school.subscription

        return ((subscription is not None and
                 subscription.is_valid()) or
                request.method in permissions.SAFE_METHODS)


class IsManager(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 1
