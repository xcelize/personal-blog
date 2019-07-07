from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/blog/')
    else:
        form = SignUpForm()
    return render(request, 'authentification/signup.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', False)
            password = request.POST.get('password', False)
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
        return redirect('/blog/')
    else:
        form = LoginForm()
    return render(request, 'authentification/login.html', {
        'form': form
    })


def log_out(request):
    logout(request)
    return redirect('/blog/')
