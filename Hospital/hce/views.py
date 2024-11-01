from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Equipo, Responsable
from .forms import EquipoForm
# Create your views here.

def inicio (request):
     return render(request,'pages/index.html')

def ingresar (request): #análogo a crear
     infoEquipo=EquipoForm(request.POST or None)
     if infoEquipo.is_valid():
          infoEquipo.save()
          return redirect('Equipos')
     return render(request,'Equipos/ingresar.html')

def Equipos(request):
    equipo = Equipo.objects.all() #trae el objeto con toda su informacion
    return render(request ,  'Equipos/index.html', {'equipos':equipo}) #captura la información desde la base de datos

def borrar(request, id):
    equipo = Equipo.objects.get(id=id)
    equipo.delete()
    return redirect('Equipos')

def editar(request, id):
    equipo = Equipo.objects.get(id=id)
    formEquipo = EquipoForm(request.POST or None, request.FILES or None, instance=equipo)
    if formEquipo.is_valid() and request.method == 'POST':
        formEquipo.save()
        messages.success(request, 'La información se actualizó correctamente.')

        return redirect('Equipos')
    return render(request, 'Equipos/editar.html' , {'formEquipo':formEquipo})

