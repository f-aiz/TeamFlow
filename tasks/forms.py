from django import forms
from .models import Project, Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'owner', 'description']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed', 'assigned_to']
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
