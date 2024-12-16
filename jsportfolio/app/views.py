from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Project, ContactMessage


def home(request):
    projectsx = Project.objects.all()
    return render(request, 'index.html', {'projects': projectsx})

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


def project_details(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'service_detail.html', {'project': project})
