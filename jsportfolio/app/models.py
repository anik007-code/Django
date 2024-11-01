from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'Message from {self.name} ({self.email})'



class Service(models.Model):
    title = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=50, default="ti-vector")
    short_description = models.TextField()
    detailed_description = models.TextField()

    def __str__(self):
        return self.title
