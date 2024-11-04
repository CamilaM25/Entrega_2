from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('Equipos/ingresar',views.ingresar,name='ingresar'),
    path('Equipos',views.Equipos,name='Equipos'),
<<<<<<< HEAD
    path('Equipos/editar/<int:id>',views.editar,name='editar'),
    path('borrar/<int:id>' , views.borrar, name='borrar'),
=======
    path('Equipos/editar/<int:id>/',views.editar,name='editar'),
    path('borrar/<int:id>/' , views.borrar, name='borrar'),
    path('Responsables' , views.Responsables, name='Responsables'),
    path('Responsables/crear' , views.Responsablescrear, name='Responsablescrear'),

>>>>>>> 43533a4d6a6bbfedd651869e8c17416edb4ff97a

]