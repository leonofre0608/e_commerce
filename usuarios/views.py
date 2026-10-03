import json 

from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def lista_usuarios(request):
    usuarios = User.objects.all().order_by ('username')
    return render (request, 'usuarios/lista_usuarios.html',{'usuarios':usuarios})


def crear_usuario (request):
    if request.method == 'POST':
        usuario = request.POST.get("usuario", "").strip()
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        
        errores = {}
        
        if not usuario:
            errores["usuario"] = "El usuario es obligatorio"
        elif User.objects.filter(username = usuario).exists():
            errores["usuario"] = "El usuario ya esta registrado"
            
        if not email:
            errores["email"] = "Debe ingresar un email valida"
            
        if not password or len(password) < 8:
            errores["password"] = "El password debe ser obligatorio y mayor a 8"
            
        if errores:
            return render (request,'usuarios/crear_usuario.html',{
                'errores': errores,
                'datos' : request.POST,
            })
        
        User.objects.create_user(
            username = usuario,
            email = email,
            first_name = first_name,
            last_name = last_name,
            password = password,
        )
        return redirect("usuarios:lista_usuarios")

    return render (request,'usuarios/crear_usuario.html')


# @csrf_exempt
# @require_POST
# def crear_usuario(request):
#     try:
#         data = json.loads(request.body)
#     except json.JSONDecodeError:
#         return JsonResponse({"Error", "no se pudo gestionar el Json."})
    
#     usuario = data.get("usuario","").strip()
#     email = data.get("email","").strip()
#     password = data.get("password","").strip()

#     errores = {}
    
#     if not usuario:
#         errores["usuario" ] = "El usuario debe ser obligatorio"
#     if not email:
#         errores["email" ] = "El email debe ser obligatorio"
#     if not password or len(password) <8 :
#         errores["password" ] = "El pasword debe ser obligatorio y debe tener almenos 8 caracteres."
        
#     if errores:
#         return JsonResponse(errores, status=400)
    
#     print({"mensaje": "usuario creado correctamente.", "usuario":
#             {usuario}, "email": {email}, "password":{password}}
#             )
    
#     return JsonResponse(
#         {"mensaje": "usuario creado correctamente.", "usuario":
#         usuario, "email": email, "password":password}, status=201
        
#     )
