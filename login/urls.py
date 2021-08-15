from django import urls
from django.urls import path
from django.urls import path
from .views import UserLogin

urlpatterns = [
    path('', UserLogin.as_view(), name='login'),
]