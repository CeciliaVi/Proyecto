from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoticiaForm, LoginForm, RegistroForm, ComentarioForm
from .models import Noticia, Categoria, Comentario
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    noticias_list = Noticia.objects.all()
    paginator = Paginator(noticias_list, 1)  # Cambia 10 por el número deseado de noticias por página
    page = request.GET.get('page')
    noticias = paginator.get_page(page)
    return render(request, 'index.html', {'noticias': noticias})

def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = NoticiaForm()
    return render(request, 'crear_noticia.html', {'form': form})

def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'lista_noticias.html', {'noticias': noticias})

def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('posts:lista_noticias')
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'editar_noticia.html', {'form': form})

def eliminar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('posts:lista_noticias')
    return render(request, 'eliminar_noticia.html', {'noticia': noticia})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('posts:index')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})

@login_required
def detalle_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    categorias = noticia.categorias.all()
    return render(request, 'detalle_noticia.html', {'noticia': noticia, 'categorias': categorias})

def categoria_view(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    # Puedes realizar cualquier lógica adicional relacionada con la vista de la categoría aquí
    return render(request, 'categoria.html', {'categoria': categoria})

def agregar_comentario(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            contenido = form.cleaned_data['contenido']

            # Si el usuario está autenticado, usamos su nombre
            if request.user.is_authenticated:
                nombre = request.user.username
            elif nombre == 'Anónimo':
                # Si no está autenticado y se seleccionó "Anónimo", dejamos el nombre como está
                pass

            comentario = Comentario(noticia=noticia, nombre=nombre, contenido=contenido)
            comentario.save()
            return redirect('posts:detalle_noticia', noticia_id=noticia_id)
    else:
        form = ComentarioForm()

    return render(request, 'agregar_comentario.html', {'form': form})
