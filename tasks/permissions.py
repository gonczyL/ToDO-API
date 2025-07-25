from rest_framework.permissions import BasePermission

class HasSessionToken(BasePermission):
    def has_permission(self, request, view):
        token = request.session.get('auth_token')
        print(f"Session Token: {token}")
        return token is not None
