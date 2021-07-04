from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Destino(models.Model):
    codigo_destino = models.IntegerField()
    calification = models.FloatField()
    users = models.ManyToManyField(User)
