from django.db import models

# Create your models here.

class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.CharField(max_length=2000)
    fecha = models.DateTimeField('Fecha de Publicacion')

class Comentario(models.Model):
    entrada = models.ForeignKey(Entrada)
    contenidocomentario = models.CharField(max_length=1000)
