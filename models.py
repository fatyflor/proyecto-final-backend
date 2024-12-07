from django.db import models
from django.utils.timezone import now

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    publicado = models.DateField()


    def __str__(self):
        return self.titulo