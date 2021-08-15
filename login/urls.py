from django import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import UserLogin

urlpatterns = [
    path('', UserLogin, name='client_home'),
]