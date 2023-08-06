from django.contrib import admin
from django.urls import path, include
from apps.posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  
    path('posts/', include('apps.posts.urls')),  
]








