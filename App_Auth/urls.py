from django.urls import path
from . import views

app_name = 'App_Auth'

urlpatterns = [
    path('', views.home, name='home'),
    # path('signup/', views.signup_view, name='signup'),
    # path('signin/', views.signin_view, name='signin'),
    # path('signout/', views.signout_view, name='signout'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
]


