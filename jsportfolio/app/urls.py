from django.urls import path
from . import views
from .views import contact

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', contact, name='contact'),

]