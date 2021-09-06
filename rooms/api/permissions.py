from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from schools.models import School


class IsSchoolManagerRUD(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return obj.school.manager == request.user


class IsSchoolManagerCL(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            kwarg_slug = request.parser_context['kwargs']['slug']
            school = get_object_or_404(School, slug=kwarg_slug)
        except Exception:
            return False

        return school.manager == request.user