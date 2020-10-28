from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from mainapp.forms import RegisterForm

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html',{
        'title': 'Inicio'
    })

def about(request):
    return render(request, 'mainapp/about.html',{
        'title': 'Acerca'
    })

def register_user(request):

    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Te has registrado correctamente')

                return redirect('articles')

        return render(request, 'mainapp/register.html', {
            'register_form': register_form
        })

def login_user(request):

    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.warning(request, 'Usuario no identificado')

        return render(request, 'mainapp/login.html', {
        })

def logout_user(request):
    logout(request)
    return redirect('login')
