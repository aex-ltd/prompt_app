from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, LoginForm

User = get_user_model()


# signup view 
def signup_view(request):
    # check if user is authenticated already 
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    # check if the request method is a post method 
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # try to create user account is the datas are valid 
            try:
                user = User.objects.create_user(
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                user.save()
                messages.success(request, "Registration Successful!")
                return redirect('login')
            
            except Exception as e:
                messages.info(request, "Unable to create account at the moment. Please try again later")
                return render(request, 'auth/signup.html', {'form':form})

        messages.error(request, "Registration failed. Please make  sure all fields are correctly filled!")
        return render(request, 'auth/signup.html', {'form':form})
    
    form = SignupForm()
    return render(request, 'auth/signup.html', {'form':form})

# login view 
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Login successful")
                    return redirect('dashboard')
                
                messages.info(request, 'Account is inactive. Please contact the admin')
                return render(request, 'auth/login.html', {'form':form})
            
            messages.error(request, "Incorrect login details")
            return render(request, 'auth/login.html', {'form':form})
        
        messages.error(request, 'Invalid login details')
        return render(request, 'auth/login.html', {'form':form})
    
    form = LoginForm()
    return render(request, 'auth/login.html', {'form':form})


# logout request
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')