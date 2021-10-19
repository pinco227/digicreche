from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from schools.models import School


class IsSchoolManagerParentTeacherRUD(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.user.is_authenticated and (
            obj.school.manager == request.user or (
                request.method in permissions.SAFE_METHODS and
                obj.room is not None and
                (request.user in obj.room.teachers.all() or
                 (request.user in obj.parents.all()))
            )
        )


class IsSchoolManagerOrParentRUD(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.user.is_authenticated and (
            obj.school.manager == request.user or
            request.user in obj.parents.all()
        )


class IsSchoolManagerTeacherSafe(permissions.BasePermission):

    def has_permission(self, request, view):

        try:
            kwarg_slug = request.parser_context['kwargs']['slug']
            school = get_object_or_404(School, slug=kwarg_slug)
        except Exception:
            return False

        return request.user.is_authenticated and (
            school.manager == request.user or (
                request.method in permissions.SAFE_METHODS and
                request.user.user_type == 2 and
                request.user.school == school
            )
        )


class IsSchoolManager(permissions.BasePermission):

    def has_permission(self, request, view):

        try:
            kwarg_slug = request.parser_context['kwargs']['slug']
            school = get_object_or_404(School, slug=kwarg_slug)
        except Exception:
            return False

        return request.user.is_authenticated and school.manager == request.user
