from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def nombre_archivo_incluye_extension(instance, filename):
    return "img/{0}".format(filename)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(Categoria, related_name='noticias')
    etiquetas = models.ManyToManyField(Etiqueta)  # Agrega esta línea para las etiquetas
    imagen = models.ImageField(upload_to='noticias/', null=True, blank=True)
    autor = models.CharField(max_length=100, blank=True, null=True)  # Campo opcional

    def __str__(self):
        return self.titulo

from django.utils import timezone

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.CharField(max_length=100, blank=True, null=True, default='')
    fecha_creacion = models.DateTimeField(default=timezone.now)  # Agrega este campo

    def __str__(self):
        return f"Comentario {self.id} de {self.nombre} en {self.noticia}"






    




    
    




