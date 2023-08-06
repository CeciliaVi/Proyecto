from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_noticia/', views.crear_noticia, name='crear_noticia'),
    path('lista_noticias/', views.lista_noticias, name='lista_noticias'), 
    path('editar_noticia/<int:pk>/', views.editar_noticia, name='editar_noticia'),
    path('eliminar_noticia/<int:pk>/', views.eliminar_noticia, name='eliminar_noticia'),
    path('login/', views.iniciar_sesion, name='login'),
    path('registro/', views.registro, name='registro'),
    path('posts/noticia/<int:noticia_id>/', views.detalle_noticia, name='detalle_noticia'),
    path('categoria/<int:pk>/', views.categoria_view, name='categoria'),
    path('agregar_comentario/<int:noticia_id>/', views.agregar_comentario, name='agregar_comentario'),
]


