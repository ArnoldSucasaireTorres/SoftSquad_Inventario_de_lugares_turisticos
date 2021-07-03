from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Destino(models.Model):
    id = models.IntegerField()
    calification = models.FloatField()
    usersCalificated = models.ManyToManyField(User)