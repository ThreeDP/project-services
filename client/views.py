from django.views.generic import TemplateView

class HomeService(TemplateView):
    template_name = 'home.html'

class ClientProfile(TemplateView):
    template_name = 'profile.html'

