from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from registerhere.models import Products


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already used.")
                return redirect('register')
            elif User.objects.filter(username=name).exists():
                messages.info(request, "Name already used.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=name, password=password, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password Not the Same")
            return redirect('register')
    else:
        return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            print("User authenticated:", user.username)
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def extends_after_home(request):
    return render(request, 'extends.html')

def products_list(request):
    products = Products.objects.all()
    return render(request, 'extends.html', {'products' : products})

def products_details(request, slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request, 'products_details.html', {'product': product})

