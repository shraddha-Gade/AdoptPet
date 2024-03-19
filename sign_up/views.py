from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group, Permission
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import CustomUser
from django.contrib.auth.views import LogoutView

# Logout view
logout_view = LogoutView.as_view(next_page = 'home')

# Create your views here.
def sign_up(request):
    return render(request, 'sign_up.html')

def login_user(request):
    return render(request, 'login_form.html')

def login_view(request):
    if request.method == 'POST':
        # Retrieve username and password from POST request
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # If user is authenticated, log the user in
            login(request, user)
            # Redirect to a different page (e.g., home page) after successful login
            return redirect('home')  # Replace 'home' with the URL name of your desired page
        else:
            # If authentication fails, return an error message or render the login form again
            return render(request, 'login_form.html', {'error_message': 'Invalid username or password'})

    # If the request method is GET, render the login form
    return render(request, 'login_form.html')

# views.py


def signup_submit(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('user_name')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        
        # Create a new CustomUser object and save it to the database
        user = CustomUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            contact_no=contact_no,
            email=email,
            password=password,
            gender=gender,
            city=city
        )
        
        # Optionally, you can log the user in after registration
        #user = authenticate(username=username, password=password)
        #login(request, user)
        
        # Redirect the user to a different page after successful registration
        return redirect('home')  # Replace 'home' with the URL name of your desired page

    # If the request method is GET, render the registration form
    return render(request, 'sign_up.html')
