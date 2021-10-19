from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from schools.models import School


class IsManagerOrListOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.user_type == 1 or
            request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (
            obj.manager == request.user or
            request.method in permissions.SAFE_METHODS)


class IsSchoolManagerOrTeacher(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            kwarg_slug = request.parser_context['kwargs']['slug']
            school = get_object_or_404(School, slug=kwarg_slug)
        except Exception:
            return False

        return ((request.user.is_authenticated and
                request.user.user_type == 1 and
                school.manager == request.user) or
                (request.user.is_authenticated and
                 request.user.user_type == 2 and
                 request.user.school == school))
