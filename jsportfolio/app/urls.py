from django.urls import path
from . import views
from .views import contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', contact, name='contact'),
    path('project/<int:project_id>/', views.project_details, name='project_details'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)