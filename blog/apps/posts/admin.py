from django.contrib import admin
from .models import Categoria, Etiqueta, Noticia
from .models import Comentario


admin.site.register(Categoria)
admin.site.register(Etiqueta)
admin.site.register(Noticia)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    # Define las columnas que quieres mostrar en la lista de comentarios
    list_display = ['id', 'nombre', 'contenido']