from django.db import models
from django.contrib.auth.models import User


# Modelo Destino
# codigo_destino: Almacena el codigo del destino del archivo JSON
# calificacion: Almacena la calificacion que tiene el destino 
# usuarios: Almacena los usuarios que ya calificaron este destino
class Destino(models.Model):
    codigo_destino = models.IntegerField()
    calificacion = models.FloatField(default=0)
    usuarios = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return str(self.codigo_destino)
