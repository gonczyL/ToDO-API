from django.contrib import admin
from django.urls import path

from tasks.views import LoginView, UserListView, TaskListCreateView, TaskDetailView

urlpatterns = [
    path('login', LoginView.as_view()),
    path('users', UserListView.as_view()),
    path('users/<int:user_id>/tasks', TaskListCreateView.as_view()),
    path('users/<int:user_id>/tasks/<int:task_id>', TaskDetailView.as_view()),
]

