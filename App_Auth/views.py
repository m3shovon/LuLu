from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, AdminLoginForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from App_Auth import models as App_AuthModel
from App_Auth import forms as App_AuthForms
from django.db.models import Subquery, OuterRef, Value
from django.db.models.functions import Coalesce
from App_Task.models import Notes
from django.db.models import Q
from django.contrib.auth.models import User

# Home
@login_required
def home(request):
    notes = Notes.objects.all().order_by('-created_at')
    total_notes_count = notes.count()
    in_progress_notes = notes.filter(is_completed=False)
    in_progress_count = notes.filter(is_completed=False).count()
    completed_count = notes.filter(is_completed=True).count()
    return render(request, "App_Auth/home.html", {
        'notes': notes,
        'total_notes_count': total_notes_count,
        'in_progress_count': in_progress_count,
        'in_progress_notes': in_progress_notes,
        'completed_count': completed_count,
    })


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('App_Auth:home')
        else:
            # messages.error(request, 'Invalid login credentials')
            error_message = 'Invalid email or password. Please try again.'
            return render(request, 'App_Auth/login.html', {'error_message': error_message })
    else:
        return render(request, 'App_Auth/login.html')

def user_logout(request):
    logout(request)
    return redirect('App_Auth:login')

# 404 Error
def handle_not_found(request,exception):
	return render(request, "App_Auth/404.html", status=404)



# def signup_view(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account created successfully! Please log in.')
#             return redirect('App_Auth:signin')
#     else:
#         form = SignupForm()

#     return render(request, 'App_Auth/signup.html', {'form': form})

# def signin_view(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('App_Hotel:home')  # Redirect to home after login
#             else:
#                 messages.error(request, 'Invalid email or password.')
#     else:
#         form = LoginForm()

#     return render(request, 'App_Auth/signin.html', {'form': form})

# @login_required
# def signout_view(request):
#     logout(request)
#     return redirect('App_Auth:signin')  


# ######### +++++++++++++++++++++ ADMIN PANEL +++++++++++++++++++++ #########

def is_admin(user):
    return user.is_authenticated and user.is_staff and user.is_superuser

def admin_logout_view(request):
    logout(request)
    return redirect('App_Auth:admin-login')  

def admin_login_view(request):
    if request.method == 'POST':
        form = AdminLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                if user.is_staff and user.is_superuser:  
                    login(request, user)
                    return redirect('App_Auth:dashboard')  
                else:
                    messages.error(request, 'Access denied. Admin only.')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = AdminLoginForm()
    return render(request, 'App_Admin/login.html', {'form': form})

