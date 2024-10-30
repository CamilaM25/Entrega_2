from django.urls import path
from .import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('Ingresar',views.ingresar,name='Ingresar'),
    path('Equipos',views.Equipos,name='equipos'),
]