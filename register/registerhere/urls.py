from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from registerhere.views import *

urlpatterns = [
    path('', register, name='register'),
    path('login', login, name='login'),
    path('home', home, name='home'),
    path('extends', extends_after_home, name='extends'),
    path('products', products_list, name='products'),
    path('products_details/<str:slug>', products_details, name='products_details'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
