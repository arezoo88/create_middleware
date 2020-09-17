from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import authenticate, logout, login


def index(request):
    print('Index Page...')
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home:index')

    else:
        form = UserLoginForm()
    return render(request, 'home/login.html', {'form': form})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home:index')
