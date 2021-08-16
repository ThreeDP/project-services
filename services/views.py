from django.views.generic import ListView
from .models import Servico

class ServicePageView(ListView):
    model = Servico
    template_name = 'service.html'
    context_object_name = 'services' # É o rotulo para lista que é enviada ao template
