from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import HasSessionToken


class UserListView(APIView):
    permission_classes = [HasSessionToken]
    def get(self, request):
        response = requests.get(
            'https://reqres.in/api/users',
            headers={
                'x-api-key': 'reqres-free-v1',
                'Content-Type': 'application/json'
            }
        )
        return Response(response.json())


class LoginView(APIView):
    def post(self, request):
        try:
            login_data = request.data
            response = requests.post(
                'https://reqres.in/api/login',
                json=login_data,
                headers={
                    'x-api-key': 'reqres-free-v1',
                    'Content-Type': 'application/json'
                }
            )

            if response.status_code == 200:
                token = response.json().get('token')

                # Csak ide mentjük:
                request.session['auth_token'] = token

                return Response({'token': token})

            return Response(response.json(), status=response.status_code)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [HasSessionToken]
    
    def get_queryset(self):
        return Task.objects.filter(user_id=self.kwargs['user_id'])

    def perform_create(self, serializer):
        serializer.save(user_id=self.kwargs['user_id'])

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'task_id'
    permission_classes = [HasSessionToken]

    def get_queryset(self):
        return Task.objects.filter(user_id=self.kwargs['user_id'])


class LogoutView(APIView):
    def post(self, request):
        request.session.flush()  # törli az egész session-t
        return Response({"message": "Logged out successfully"})