from rest_framework import permissions


# Custom permission class that allows read-only access to non-admin users
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write (POST, PUT, PATCH, DELETE) methods only for admin users
        return bool(request.user and request.user.is_staff)