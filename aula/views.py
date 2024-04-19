from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Estudiante
# Create your views here.

def home(request):
    return render(request, 'home.html')


def añadir_pag(request):
    return render(request, 'añadir_pag.html')

def listado(request):
    estudiante = Estudiante.objects.all
    
    return render(request, 'listado.html', {
        'estudiante': estudiante
    })
    
def añadir_est(request):
    cedula = request.POST['cedula']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    
    estudiante = Estudiante.objects.create(cedula = cedula, nombre = nombre, apellido = apellido)
    return redirect('/')

def editar_pag(request,cedula):
    estudiante = Estudiante.objects.get(cedula = cedula)
    return render(request, 'editar_pag.html', {'estudiante': estudiante})

def editar_est(request):
    cedula = request.POST['cedula']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    estudiante = Estudiante.objects.get(cedula = cedula)
    estudiante.nombre = nombre
    estudiante.apellido = apellido
    estudiante.save()

    return redirect('/listado/')

def eliminar(request,cedula):
    estudiante = Estudiante.objects.get(cedula = cedula)
    estudiante.delete()

    return redirect('/listado/')