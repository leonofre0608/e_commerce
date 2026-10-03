from django.urls import path

from . import views 

app_name = "usuarios" 
urlpatterns  = [
    # path("crear/", views.crear_usuario, name="crear_usuario")
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('crear-usuario', views.crear_usuario, name='crear_usuario'),
    ]
