from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('', views.project_list, name='project_list'),  # List of all projects
    path('create/', views.project_create, name='project_create'),  # Create a new project
    path('<int:pk>/', views.project_detail, name='project_detail'),  # View project details
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),  # Delete a project
    path('<int:project_id>/tasks/', views.task_list, name='task_list'),  # List of tasks for a specific project
    path('<int:project_id>/tasks/create/', views.task_create, name='task_create'),  # Create a new task within a project
    path('<int:project_id>/tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),
]
