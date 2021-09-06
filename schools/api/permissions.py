from rest_framework import permissions


class IsManagerOrListOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return obj.manager == request.user
