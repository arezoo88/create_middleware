from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import authenticate, logout, login
from .models import Person
from django.db.models import Q
from .forms import SearchForm
from django.db.models.functions import Greatest
# use search vector
from django.contrib.postgres.search import SearchVector, TrigramSimilarity


def index(request):
    persons = Person.objects.all()
    form = SearchForm()
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data['search']
            # persons = persons.filter(Q(name__icontains=cd) | Q(description__icontains=cd))
            # persons = persons.annotate(search = SearchVector('name','description')).filter(search=cd) #daghighan hamun kalameha
            # persons = persons.annotate(similarity=TrigramSimilarity('name', cd), ).filter(similarity__gt=0.3) \
            #     .order_by('-similarity')
            persons = persons.annotate(similarity=Greatest(TrigramSimilarity('name', cd), TrigramSimilarity('description', cd))).filter(similarity__gte=0.1).order_by('-similarity')
    return render(request, 'home/index.html', {'persons': persons, 'form': form})


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
