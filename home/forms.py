from django.contrib.auth.models import User

from django import forms


# Create the form User Table
class UserLoginForm(forms.Form):
    # class Meta:
    #     model = User
    #
    #     fields = ['username', 'password']
    username = forms.CharField(label='Your name', max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=40,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class SearchForm(forms.Form):
    search = forms.CharField()
