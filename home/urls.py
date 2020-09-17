from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
]