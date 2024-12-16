from ckeditor.fields import RichTextField
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'Message from {self.name} ({self.email})'


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # description = RichTextField()
    icon_class = models.CharField(max_length=50, default="ti-vector")
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)


    def __str__(self):
        return self.name