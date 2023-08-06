from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Noticia
from django.contrib.auth.models import User
from .models import Comentario

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'contenido', 'categorias')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico')  # Agregamos el campo de email al formulario

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)  # Incluir el campo de email en el formulario de registro
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'contenido']  # Incluye los campos 'nombre' y 'contenido' en el formulario