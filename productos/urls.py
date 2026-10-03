
from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('crear/', views.crea_producto, name='crea_producto'),
    path('api/productos/', views.listar_productos, name='listar_productos'),
    path('api/productos/crear/', views.crear_producto, name='crear_producto'),
    path('api/eliminar/<int:producto_id>/', views.api_eliminar_producto, name='api_eliminar'),
]