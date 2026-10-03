from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Producto

def lista_productos(request):
    return render(request, 'lista.html')

def crea_producto(request):
    return render(request, 'crear.html')

def listar_productos(request):
    productos = Producto.objects.all().order_by('id')
    data = []
    for p in productos:
        data.append({
            'id': p.id,
            'nombre': p.nombre,
            'precio': str(p.precio),
            'descripcion': p.descripcion or '',
            'imagen_url': p.imagen.url if p.imagen else ''
        })
    return JsonResponse(data, safe=False)

@csrf_exempt
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')

        producto = Producto.objects.create(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            imagen=imagen
        )

        return JsonResponse({
            'mensaje': 'Producto creado con éxito',
            'id': producto.id
        }, status=201)
    return JsonResponse({'error': 'Método no permitido'}, status= 405)

@csrf_exempt
def api_eliminar_producto(request, producto_id):
    """Elimina un producto por su ID."""
    if request.method == 'DELETE' or request.method == 'POST':
        try:
            producto = Producto.objects.get(id=producto_id)
            
            # Borrar la imagen de la carpeta media si existe (opcional pero recomendado)
            if producto.imagen:
                producto.imagen.delete(save=False)
                
            producto.delete()
            return JsonResponse({'mensaje': 'Producto eliminado correctamente'})
        except Producto.DoesNotExist:
            return JsonResponse({'error': 'Producto no encontrado'}, status=404)

    return JsonResponse({'error': 'Método no permitido'}, status=405)