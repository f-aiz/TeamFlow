from django.contrib import admin
from .models import Project, Task

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at', 'owner')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'completed', 'project', 'assigned_to')
    list_filter = ('completed', 'due_date')
    search_fields = ('title', 'description')
