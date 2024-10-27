from app.models import ContactMessage
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not all([name, email, message]):
            messages.error(request, "All fields are required.")
            return redirect('contact')

        values = ContactMessage(name=name, email=email, message=message)
        values.save()

        messages.success(request, "Your message was sent successfully.")
        return redirect('home')

    return render(request, 'index.html')