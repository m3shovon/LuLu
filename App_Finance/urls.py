
from django.urls import path
from . import views

app_name = 'App_Finance'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('expense/new/', views.add_expense, name='add_expense'),
    path('budget/new/', views.add_budget, name='add_budget'),
]
