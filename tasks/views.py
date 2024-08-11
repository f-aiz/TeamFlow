from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Project
from .forms import ProjectForm, TaskForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.shortcuts import render
from django.contrib import messages

import logging

logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('project_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def task_list(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = project.tasks.all()
    return render(request, 'tasks/task_list.html', {'project': project, 'tasks': tasks})

@login_required
def task_create(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('task_list', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'project': project})

@login_required
def task_delete(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id, project_id=project_id)
    task.delete()
    return redirect(reverse('task_list', args=[project_id]))

@login_required
def project_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    projects = Project.objects.all()
    messages.info(request, 'You are logged in as {}'.format(request.user.username))
    return render(request, 'tasks/project_list.html', {'projects': projects})
@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')  # Adjust this if necessary
    else:
        form = ProjectForm()
    return render(request, 'tasks/project_form.html', {'form': form})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'tasks/project_detail.html', {'project': project})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'tasks/project_confirm_delete.html', {'project': project})
