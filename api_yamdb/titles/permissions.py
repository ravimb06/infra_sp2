from rest_framework import permissions


class AdminOrReadOnly(permissions.BasePermission):
    """Проверка - является ли пользователь администратором."""
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or (
            request.user.is_admin and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or (
            request.user.is_admin and request.user.is_authenticated
        )
