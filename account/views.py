from django.shortcuts import render

# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from django.contrib.auth.views import LogoutView

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base:index')  # replace 'home' with your home page URL
    else:
        form = SignUpForm()
    return render(request, 'account/register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('base:index')
    
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('base:index')  # replace 'home' with your home page URL
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


class CustomLogoutView(LogoutView):
    def get_next_page(self):
        return redirect('base:index') 

