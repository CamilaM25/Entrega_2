from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('Equipos/equipo',views.equipo,name='equipo'),
    path('Responsables/responsable',views.responsable,name='responsable'),
    path('Equipos/ingresar',views.ingresar,name='ingresar'),
    #CRUD equipos
    path('Equipos',views.Equipos,name='Equipos'), 
    path('Equipos/editar/<int:id>',views.editar,name='editar'),
    path('borrar/<int:id>' , views.borrar, name='borrar'),
    path('Equipos/editar/<int:id>/',views.editar,name='editar'),
    path('borrar/<int:id>/' , views.borrar, name='borrar'),
    path('Equipos/ver/<int:id>/', views.ver, name='ver'),

    #CRUD responsables
    path('Responsables' , views.Responsables, name='Responsables'),
    path('Responsables/crear' , views.Responsablescrear, name='Responsablescrear'),
    path('Responsables/editarResponsable/<int:id>',views.editarResponsable, name='editarResponsable'),
    path('borrarResponsable/<int:id>/' , views.borrarResponsable, name='borrarResponsable'),

    
    #secciones
    path('Equipos/biomedica', views.Biomedica, name='Biomedica'),
    path('Equipos/infraestructura', views.Infraestructura, name='Infraestructura'),
    path('Equipos/sistemas', views.Sistemas, name='Sistemas'),
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)