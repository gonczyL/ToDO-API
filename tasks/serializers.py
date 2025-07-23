from rest_framework import permissions
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {
            'user_id': {'required': False}
        }

class TokenAuthPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return 'Authorization' in request.headers
