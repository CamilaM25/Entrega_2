from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Equipo, Responsable
from .forms import EquipoForm,ResponsableForm
# Create your views here.

def inicio (request):
     return render(request,'pages/index.html')

def equipo (request):
    return render (request, 'Equipos/equipo.html')

def responsable (request):
    return render (request, 'Responsables/responsable.html')

#CRUD PARA EQUIPOS
def Equipos(request):
    equipo = Equipo.objects.all() #trae el objeto con toda su informacion
    return render(request , 'Equipos/index.html', {'equipos':equipo}) #captura la información desde la base de datos


def ingresar (request):
     infoEquipo=EquipoForm(request.POST, request.FILES or None)
     asignarResponsable=Responsable.objects.all()
     if infoEquipo.is_valid():
          infoEquipo.save()
          return redirect('Equipos')
     return render(request,'Equipos/ingresar.html',{'Responsables':asignarResponsable})

def editar(request, id):
    equipo = Equipo.objects.get(id=id)
    asignarResponsable = Responsable.objects.all() 
    formEquipo = EquipoForm(request.POST or None, request.FILES or None, instance=equipo)

    # Prellenar el campo "Responsable" con la ID del responsable actual
    if formEquipo.is_valid() and request.method == 'POST':
        formEquipo.save()
        Area=equipo.Area
        return render(request, 'Equipos/ver.html', {'equipo': equipo, 'area': Area})

    return render(request,'Equipos/editar.html', {
        'formEquipo': formEquipo,
        'Responsables': asignarResponsable,
        'responsable_actual': equipo.Responsable  
    })

def ver (request,id):
    equipo = Equipo.objects.get(id=id) #Busca el Id
    return render(request, 'Equipos/ver.html', {'equipo': equipo})

def borrar(request, id):
    equipo = Equipo.objects.get(id=id)
    equipo.delete()
    return redirect('Equipos')


#secciones para cada área de equipos

def Biomedica(request):
    equipo = Equipo.objects.all() #trae el objeto con toda su informacion
    return render(request , 'Equipos/biomedica.html', {'equipos':equipo}) #captura la información desde la base de datos
def Infraestructura(request):
    equipo = Equipo.objects.all() #trae el objeto con toda su informacion
    return render(request , 'Equipos/infraestructura.html', {'equipos':equipo}) #captura la información desde la base de datos
def Sistemas(request):
    equipo = Equipo.objects.all() #trae el objeto con toda su informacion
    return render(request , 'Equipos/sistemas.html', {'equipos':equipo}) #captura la información desde la base de datos


#CRUD para responsables

def Responsables(request):
     asignarResponsable = Responsable.objects.all() 
     return render(request,'Responsables/index.html',{'Responsables':asignarResponsable})

def Responsablescrear(request):
    infoEquipo = ResponsableForm(request.POST or None)
    if infoEquipo.is_valid():
        infoEquipo.save()
        return redirect('Responsables')
    else:
        print(infoEquipo.errors)  # Muestra errores del formulario para depuración
    return render(request, 'Responsables/crear.html', {'form': infoEquipo})

def editarResponsable(request, id):
    responsable = Responsable.objects.get(id=id)
    formResponsable = ResponsableForm(request.POST or None, request.FILES or None, instance=responsable)

    if formResponsable.is_valid() and request.method == 'POST':
        formResponsable.save()
        return redirect('Responsables')

    return render(request,'Responsables/editarResponsable.html', {
        'formResponsable': formResponsable,
        
    })


def borrarResponsable(request, id):
    responsable = Responsable.objects.get(id=id)
    responsable.delete()
    return redirect('Responsables')

