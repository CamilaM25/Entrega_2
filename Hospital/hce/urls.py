from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('Equipos/ingresar',views.ingresar,name='ingresar'),
    path('Equipos',views.Equipos,name='Equipos'),
    path('Equipos/editar/<int:id>',views.editar,name='editar'),
    path('borrar/<int:id>' , views.borrar, name='borrar'),
    path('Equipos/editar/<int:id>/',views.editar,name='editar'),
    path('borrar/<int:id>/' , views.borrar, name='borrar'),
    path('Responsables' , views.Responsables, name='Responsables'),
    path('Responsables/crear' , views.Responsablescrear, name='Responsablescrear'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)