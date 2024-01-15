from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib import messages, auth


def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already used.")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already Used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password Not the Same")
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def counter(request):
    text = request.POST['text']
    amount_of_word = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_word})
