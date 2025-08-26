from rest_framework.permissions import BasePermission, SAFE_METHODS

class isHOD(BasePermission):
    """
    Custom permission to only allow Heads of Department (HOD) to access certain views.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 1

class isStaff(BasePermission):
    """
    Custom permission to only allow staff members to access certain views.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 2

class isStudent(BasePermission):
    """
    Custom permission to only allow students to access certain views.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 3

class isHODorStaff(BasePermission):
    """
    Custom permission to only allow Heads of Department (HOD) or staff members to access certain views.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type in [1, 2]

class ReadOnly(BasePermission):
    """
    Custom permission to only allow read-only access.
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

