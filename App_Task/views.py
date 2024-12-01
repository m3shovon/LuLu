# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Project, Task
# from .forms import ProjectForm, TaskForm

# def project_list(request):
#     projects = Project.objects.all()
#     return render(request, 'App_Task/project_list.html', {'projects': projects})

# def project_detail(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     tasks = project.tasks.all()
#     return render(request, 'App_Task/project_detail.html', {'project': project, 'tasks': tasks})

# def project_create(request):
#     if request.method == 'POST':
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('App_Task:project_list')
#     else:
#         form = ProjectForm()
#     return render(request, 'App_Task/project_form.html', {'form': form})

# def task_create(request, project_id):
#     project = get_object_or_404(Project, id=project_id)
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.project = project
#             task.save()
#             return redirect('App_Task:project_detail', pk=project.id)
#     else:
#         form = TaskForm(initial={'project': project})
#     return render(request, 'App_Task/task_form.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Project, Task
from App_Auth.models import CustomerProfile
from App_Task.forms import ProjectForm, TaskForm
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
# import datetime
from datetime import datetime

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'App_Task/project_list.html', {'projects': projects})

# @login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = Task.objects.filter(project=project)
    pending_count = project.tasks.filter(status='Pending').count()
    progress_count = project.tasks.filter(status='In Progress').count()
    completed_count = project.tasks.filter(status='Completed').count()
    incompleted_count = project.tasks.filter(status='Incomplete').count()

    # Countdown
    # remaining_days = (project.end_date - datetime.date.today()).days
    # remaining_time =  str(project.end_date - datetime.datetime.now().date())
    # remaining_time = project.time_remaining().days * 24 * 60 * 60 

    context = {'project': project, 
               'tasks': tasks,
                'assigned_count': pending_count,
                'working_count': progress_count,
                'completed_count': completed_count,
                'incompleted_count': incompleted_count,
                # 'remaining_days': remaining_days,
                # 'remaining_time': remaining_time,
                
            
               }
    return render(request, 'App_Task/project_detail.html', context)


# @login_required
def project_create(request):
    # managers = Employee.objects.filter(managed_projects=True)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.admin = request.user
            # project.manager = Employee.objects.get(user=request.POST.get('manager'))
            # project.manager = request.user.employee
            project.save()
            form.save_m2m()
            messages.success(request, 'Project created successfully')
            return redirect('App_Task:project_detail', pk=project.pk)
    else:
        form = ProjectForm()

    context = {'form': form}
    return render(request, 'App_Task/create_project.html', context)


# @login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully')
            return redirect('App_Task:project_detail', pk=pk)
    else:
        form = ProjectForm(instance=project)

    context = {'form': form, 'project': project}
    return render(request, 'App_Task/edit_project.html', context)

# @login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    messages.success(request, 'Project has been deleted successfully!')
    return redirect('App_Task:project_list')

# @login_required
# def create_task(request, project_pk):
#     project = get_object_or_404(Project, pk=project_pk)

#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.project = project
#             task.save()
#             messages.success(request, 'Task created successfully')
#             return redirect('App_Task:project_detail', pk=project.pk)
#     else:
#         form = TaskForm()

#     context = {'form': form, 'project': project}
#     return render(request, 'App_Task/task_create.html', context)

def create_task(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('App_Task:project_detail', pk=project.id)
    else:
        form = TaskForm(initial={'project': project})
    context = {'form': form, 'project': project}
    return render(request, 'App_Task/task_create.html', context)


# @login_required
def edit_task(request, pk):

    task = get_object_or_404(Task, pk=pk)
    project = task.project

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save() 
            form.save_m2m() 
            messages.success(request, 'Task updated successfully')
            return redirect('App_Task:project_detail', pk=project.pk)
            # form.save()
            # messages.success(request, 'Task updated successfully')
            # return redirect('App_Task:project_detail', pk=project.pk)
    else:
        form = TaskForm(instance=task)

    context = {'form': form, 'project': project, 'task': task}
    return render(request, 'App_Task/edit_task.html', context)

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project_pk = task.project.pk  # Retrieve the project's primary key for redirection

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task has been deleted successfully!')
        return redirect('App_Task:project_detail', pk=project_pk)

    context = {'task': task}
    return render(request, 'App_Task/delete_task.html', context)

# @login_required
# def assign_task(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     project = task.project
#     if request.user.is_superuser or request.user == project.manager:
#         if request.method == 'POST':
#             form = AssignTaskForm(request.POST)
#             if form.is_valid():
#                 employees = form.cleaned_data.get('employees')
#                 task.employees.add(*employees)
#                 task.status = Task.Status.ASSIGNED
#                 task.save()
#                 messages.success(request, 'Task assigned successfully')
#                 return redirect('project_detail', project.pk)
#             else:
#                 form = AssignTaskForm()
#             return render(request, 'App_Task/assign_task.html', {'form': form, 'task': task})
#         else:
#             raise PermissionDenied


# @login_required
# def delete_task(request, pk):
#     """
#     Allows the admin or project manager to delete a task for a project
#     """
#     task = get_object_or_404(Task, pk=pk)
#     project = task.project

#     if request.user.is_superuser or request.user == project.manager:
#         if request.method == 'POST':
#             task.delete()
#             messages.success(request, 'Task deleted successfully')
#             return redirect('App_Task:project_detail', pk=project.pk)
#         else:
#             return render(request, 'App_Task/delete_task.html', {'task': task})
#     else:
#         raise PermissionDenied

# @login_required
# def tasks_by_status(request, status):
#     tasks = Task.objects.filter(status=status)
#     task_count = tasks.count()
#     return render(request, 'App_Task/tasks_by_status.html', {'tasks': tasks, 'status': status,  'task_count': task_count})


