from pupils.models import Pupil
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from schools.models import School


class IsSchoolManagerTeacherParentRUD(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.user.is_authenticated and (
            obj.pupil.school.manager == request.user or
            request.user in obj.pupil.room.teachers.all() or (
                request.method in permissions.SAFE_METHODS and
                request.user in obj.pupil.parents.all()
            )
        )


class IsSchoolManagerTeacherParentSafe(permissions.BasePermission):

    def has_permission(self, request, view):

        try:
            kwarg_slug = request.parser_context['kwargs']['slug']
            school = get_object_or_404(School, slug=kwarg_slug)

            kwarg_pk = request.parser_context['kwargs']['pk']
            pupil = get_object_or_404(Pupil, pk=kwarg_pk)
        except Exception:
            return False

        return request.user.is_authenticated and (
            school.manager == request.user or (
                request.user.user_type == 2 and
                request.user.school == school and
                request.user in pupil.room.teachers.all()
            ) or (
                request.method in permissions.SAFE_METHODS and
                request.user.user_type == 3 and
                request.user.school == school and
                request.user in pupil.parents.all()
            )
        )


class IsAdminOrSafe(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff) or (
            request.method in permissions.SAFE_METHODS)
