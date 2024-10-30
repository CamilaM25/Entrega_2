from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio (request):
     return render(request,'pages/index.htlm')

def ingresar (request):
     return render(request,'Equipos/Ingresar.htlm')

def Equipos (request):
     return render(request,'Equipos/index.htlm')