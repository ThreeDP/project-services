from django.contrib.auth.models import User
from django.db import models


class Servico(models.Model):
    service_name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True)
    service_time = models.PositiveIntegerField()
    service_price = models.FloatField()
    service_category = models.CharField(max_length=40)
    business = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.service_name[:20]