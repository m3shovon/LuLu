from django.urls import path
from App_Task import views

app_name = 'App_Task'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/new/', views.project_create, name='project_create'),
    path('project/<int:pk>/update/', views.edit_project, name='update_project'),
    path('project/<int:pk>/delete/', views.delete_project, name='delete_project'),
    


    # path('task/tasks-by-status/<str:status>/', views.tasks_by_status, name='tasks_by_status'),
    # path('task/<int:task_id>/', views.task_details, name='task_details'),


    # Add task
    path('add/', views.add_note_view, name='add_note'),
    path('edit/<int:pk>/', views.edit_note_view, name='edit_note'),
    path('delete/<int:pk>/', views.delete_note_view, name='delete_note'),
    path('mark-complete/<int:pk>/', views.mark_complete_view, name='mark_complete'),

]
