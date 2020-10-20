from django.shortcuts import render
from .models import SliderIndex,MisionyVision, Insumos


# utilzar la libreria de modelo de usuario (User)
from django.contrib.auth.models import User
# librerias de validacion de login
from django.contrib.auth import authenticate,logout, login as login_aut
# agregar un decorador que permita evitar el ingreso a paginas
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.
def index(request):
    autos = SliderIndex.objects.all()
    return render(request,'index2.html',{'autos':autos})

def galeria(request):
    return render(request,'galeria_imagenes.html')

@login_required(login_url='/login/')
@permission_required('myCar.view_insumos',login_url='/login/')
@permission_required('myCar.change_insumos',login_url='/login/')
def modificar(request):
    msg=''
    if request.POST:
        nombre = request.POST.get("txtNombreP")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescripcion")
        stock = request.POST.get("txtStock")

        try:
            insumo = Insumos.objects.get(nombre=nombre)
            insumo.precio = precio
            insumo.descripcion = descripcion
            insumo.stock = stock
            insumo.save()
            msg='Modifico'
        except:
            msg='No Modifico'

    insumos = Insumos.objects.all()
    return render(request,'admin_productos.html',{'lista_insumos':insumos,'msg':msg})

    
@login_required(login_url='/login/')
@permission_required('myCar.view_insumos',login_url='/login/')
def busqueda_mod(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)        
        return render(request,'productos_mod.html',{'insumo':insumo})
    except:
        msg='No Ubico el Insumo'
    insumos = Insumos.objects.all()
    return render(request,'admin_productos.html',{'lista_insumos':insumos,'msg':msg})


@login_required(login_url='/login/')
@permission_required('myCar.delete_insumos',login_url='/login/')
def eliminar(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        insumo.delete()
        msg='Elimino Insumo'
    except:
        msg='No Elimino Insumo'
    insumos = Insumos.objects.all()
    return render(request,'admin_productos.html',{'lista_insumos':insumos,'msg':msg})

@login_required(login_url='/login/')
@permission_required('myCar.view_insumos',login_url='/login/')
def lista_insumos(request):
    insumos = Insumos.objects.all()
    return render(request,'admin_productos.html',{'lista_insumos':insumos})

@login_required(login_url='/login/')
@permission_required('myCar.add_insumos',login_url='/login/')
def insumos(request):
    if request.POST:
        nombre = request.POST.get("txtNombreP")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescripcion")
        stock = request.POST.get("txtStock")
        insumo = Insumos(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            stock=stock
        )
        insumo.save()
        return render(request,'productos.html',{'msg':'grabo insumo'})
    return render(request,'productos.html')

def quien(request):
    myv= MisionyVision.objects.all()
    return render(request,'quienes.html',{'myv':myv})

def registro(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtCorreo")
        pass1 = request.POST.get("txtPass1")
        pass2 = request.POST.get("txtPass2")
        usuario = request.POST.get("txtUsuario")

        if pass1!=pass2:
            return render(request,'formulario_registro.html',{'msg':'contraseñas incorrectas'})
        
        try:
            usu = User.objects.get(username=usuario)
            return render(request,'formulario_registro.html',{'msg':'usuario existe'})
        except:                
            usu = User()
            usu.first_name = nombre
            usu.last_name = apellido
            usu.email = email
            usu.set_password(pass1)
            usu.username = usuario
            usu.save()

            us = authenticate(request, username=usuario, password=pass1)
            login_aut(request,us)

            autos = SliderIndex.objects.all()
            return render(request,'index2.html',{'autos':autos})

    return render(request,'formulario_registro.html')

def cerrar_sesion(request):
    logout(request)
    autos = SliderIndex.objects.all()
    return render(request,'index2.html',{'autos':autos})

def login(request):
    if request.POST:
        usuario = request.POST.get("txtNombreP")
        password = request.POST.get("txtPass")
        us = authenticate(request, username=usuario, password=password)
        if us is not None and us.is_active:
            login_aut(request,us)
            autos = SliderIndex.objects.all()
            return render(request,'index2.html',{'autos':autos}) 
        else:
            return render(request,'login.html',{'msg':'no existe'})
    return render(request,'login.html')