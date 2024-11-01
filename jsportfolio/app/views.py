from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service, ContactMessage

def home(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services': services})

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

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service_detail.html', {'service': service})
