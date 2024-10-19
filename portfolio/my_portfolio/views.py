from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from my_portfolio.models import Contact


# Create your views here.
def dashboard(request):
    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        values = Contact(name=name, email=email, desc=desc)
        values.save()
        messages.warning(request, "Your message was updated.")
        return redirect('home')
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')
