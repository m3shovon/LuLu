from django.db import models
from django.contrib.auth.models import User
from Core import settings
from datetime import datetime

class Type(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Label(models.Model):
    name = models.CharField(max_length=100)
    context = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project_type = models.CharField(max_length=100, choices=[('Personal', 'Personal'), ('Work', 'Work')], default='Personal')
    assigned_to = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='project_assigned')
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def time_remaining(self):
        current_time = datetime.now().date()
        remaining_time = self.end_date - current_time
        return remaining_time

    def time_remaining_days(self):
        remaining_time = self.time_remaining()
        return remaining_time.days

    def time_remaining_hours(self):
        remaining_time = self.time_remaining()
        total_seconds = remaining_time.total_seconds()
        hours = total_seconds // 3600
        return int(hours)

    def time_remaining_minutes(self):
        remaining_time = self.time_remaining()
        total_seconds = remaining_time.total_seconds()
        minutes = (total_seconds % 3600) // 60
        return int(minutes)

    def time_remaining_seconds(self):
        remaining_time = self.time_remaining()
        total_seconds = remaining_time.total_seconds()
        seconds = total_seconds % 60
        return int(seconds)


class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='task_assigned')
    task_type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks_type')
    label = models.ManyToManyField(Label, blank=True, related_name='task_label')
    status = models.CharField(max_length=100, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Incompleted', 'Incompleted')], default='Pending')
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Notes(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
