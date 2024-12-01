from django.urls import path
from App_Task import views

app_name = 'App_Task'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/new/', views.project_create, name='project_create'),
    path('project/<int:pk>/update/', views.edit_project, name='update_project'),
    path('project/<int:pk>/delete/', views.delete_project, name='delete_project'),
    
    path('projects/<int:project_id>/tasks/new/', views.create_task, name='task_create'),
    path('project/<int:project_pk>/create_task/', views.create_task, name='create_task'),
    path('task/<int:pk>/update/', views.edit_task, name='edit_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),

    # path('task/tasks-by-status/<str:status>/', views.tasks_by_status, name='tasks_by_status'),
    # path('task/<int:task_id>/', views.task_details, name='task_details'),
]
