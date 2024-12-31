from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def register_or_login(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            # Registration Process
            first_name = request.POST.get('first_name')  # User name
            username = request.POST.get('username')  # Email for registration
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            # Basic validations
            if password1 != password2:
                messages.error(request, "Passwords do not match.")
                return render(request, 'registerLogin.html')

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return render(request, 'registerLogin.html')

            # Create the user
            
            user = User.objects.create_user(username=username, first_name=first_name, password=password1)
            user.save()

            # Log the user in and redirect to home page
            return redirect('registerLogin')

        elif 'login_user_' in request.POST:
            # Login Process
            username = request.POST.get('username')  # Username or email for login
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                
                messages.error(request, "Invalid credentials. Please try again.")
                return render(request, 'registerLogin.html')

    return render(request, 'registerLogin.html')


# logout
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')

# login required






