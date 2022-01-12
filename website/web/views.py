from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render


def index(request):
    return render(request, 'web/base.html')


def register_view(request):
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
    return render(request, 'web/login.html', {'login_form': login_form})
