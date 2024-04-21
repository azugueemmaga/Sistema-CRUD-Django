from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
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
    

def clean_nota1(self):
        nota1 = self.cleaned_data.get('nota1')
        if nota1 and not 0 <= nota1 <= 10:
            raise ValidationError('La nota 1 debe estar entre 0 y 10')
        return nota1
def clean_nota2(self):
        nota2 = self.cleaned_data.get('nota2')
        if nota2 and not 0 <= nota2 <= 10:
            raise ValidationError('La nota 1 debe estar entre 0 y 10')
        return nota2
def clean_nota3(self):
        nota3 = self.cleaned_data.get('nota3')
        if nota3 and not 0 <= nota3 <= 10:
            raise ValidationError('La nota 1 debe estar entre 0 y 10')
        return nota3

def calcular_promedio(self):
        if self.nota1 and self.nota2 and self.nota3:
            self.promedio = (self.nota1 + self.nota2 + self.nota3) / 3
            self.save()

def añadir_est(request):
    cedula = request.POST['cedula']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    anio = request.POST['anio']
    seccion = request.POST['seccion']
    nota1 = float(request.POST['nota1']) if request.POST['nota1'] else 1.0
    nota2 = float(request.POST['nota2']) if request.POST['nota2'] else 1.0
    nota3 = float(request.POST['nota3']) if request.POST['nota3'] else 1.0

    estudiante = Estudiante.objects.create(cedula = cedula, nombre = nombre, apellido = apellido, anio = anio , seccion = seccion, nota1 = nota1, nota2 = nota2, nota3 = nota3)
    estudiante.calcular_promedio()

    context = {
    'mensaje_exito': f"Estudiante agregado con éxito: {nombre} {apellido}"
  }
    return redirect('/listado/')

def editarEstudianteModal(request,cedula):
    estudiante = Estudiante.objects.get(cedula = cedula)
    return render(request, 'editarEstudianteModal.html', {'estudiante': estudiante})


def editar_est(request):
    cedula = request.POST['cedula']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    anio = request.POST['anio']
    seccion = request.POST['seccion']
    nota1 = float(request.POST['nota1']) if request.POST['nota1'] else 1.0
    nota2 = float(request.POST['nota2']) if request.POST['nota2'] else 1.0
    nota3 = float(request.POST['nota3']) if request.POST['nota3'] else 1.0

    try:
        # Attempt to retrieve the student object using the submitted cedula
        estudiante = Estudiante.objects.get(cedula=cedula)

        # Update the student's attributes
        estudiante.nombre = nombre
        estudiante.apellido = apellido
        estudiante.anio = anio
        estudiante.seccion = seccion
        estudiante.nota1 = nota1
        estudiante.nota2 = nota2
        estudiante.nota3 = nota3

        # Recalculate and save the average after updating notes
        estudiante.calcular_promedio()

        # Save the updated student object
        estudiante.save()

        # Success message (optional)
        message = "Estudiante actualizado correctamente."

    except Estudiante.DoesNotExist:
        # Handle the case where the student doesn't exist
        message = "Error: El estudiante con la cédula indicada no existe."

    # Redirect to the desired page, passing the message as context
    return redirect('/listado/', {'message': message})

def eliminar(request,cedula):
    estudiante = Estudiante.objects.get(cedula = cedula)
    estudiante.delete()

    return redirect('/listado/')