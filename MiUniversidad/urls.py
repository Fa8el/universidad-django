# Importa las vistas desde la misma aplicación
from django.contrib import admin
from django.urls import path
from Modulos.Academica.views import formularioContacto, contactar


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('formularioContacto/', formularioContacto  ),
    path('contactar/', contactar)
   

    
]



