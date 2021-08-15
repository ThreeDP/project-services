from django.urls import path
from .views import HomeService, ClientProfile

urlpatterns = [
    path('', HomeService.as_view(), name='home-services'),
    path('profile/', ClientProfile.as_view(), name='profile'),
]