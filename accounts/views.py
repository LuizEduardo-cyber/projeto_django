from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def user_login(request):

    if request.method == "POST":

        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = authenticate(
            request,
            username=email,
            password=senha
        )

        if usuario is not None:

            login(request, usuario)

            return redirect('task_list')


    return render(request, 'accounts/login.html')

def register(request):

    if request.method == "POST":

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        User.objects.create_user(
            username=email,
            email=email,
            password=senha,
            first_name=nome
        )

        return redirect('login')


    return render(request, 'accounts/register.html')

