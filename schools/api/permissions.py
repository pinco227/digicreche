from rest_framework import permissions


class IsManagerOrListOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.user_type == 1 or
            request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return obj.manager == request.user
