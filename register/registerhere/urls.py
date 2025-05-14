from django.urls import path
from registerhere.views import *

urlpatterns = [
    path('', register, name='register'),
    path('login', login, name='login'),
    path('home', home, name='home'),
]
