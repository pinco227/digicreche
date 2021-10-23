from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from schools.models import School


class IsSchoolManagerOrTeacherParentReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        kwarg_slug = request.parser_context['kwargs']['slug']

        parent_access = False
        if request.user.user_type == 3:
            for pupil in request.user.children.all():
                if pupil.room == obj:
                    parent_access = True

        return ((obj.school.manager == request.user or (
            request.method in permissions.SAFE_METHODS and
            obj == request.user.room) or (
            request.method in permissions.SAFE_METHODS and
            request.user.user_type == 3 and parent_access)) and
            obj.school.slug == kwarg_slug)


class IsSchoolManager(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            kwarg_slug = request.parser_context['kwargs']['slug']
            school = get_object_or_404(School, slug=kwarg_slug)
        except Exception:
            return False

        return school.manager == request.user
