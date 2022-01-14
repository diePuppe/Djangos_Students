from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return render(request, 'web/base.html')


def register_view(request):   #the registerforms and also the login forms are imported from django
    register_form = UserCreationForm()
    if request.method == "POST":
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
    return render(request, 'web/register.html', {'register_form': register_form})


def login_view(request):
    login_form = AuthenticationForm()
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']  #grabing data from database
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
    return render(request, 'web/login.html', {'login_form': login_form})

def logout_view(request):
    logout(request) #logout was imported from django
    return redirect(reverse('web:index'))
