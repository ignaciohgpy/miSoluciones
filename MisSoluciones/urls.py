"""MisSoluciones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.conf.urls import url
from Soluciones.views import *
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index,name='index'),
    path('problema/<str:libro>', problema,name='problema'),
    path('cargar', cargar, name="cargar"), #OK
    path('contac/', contac, name="contac"), #OK
    path('formaPKT/', formaPket, name="formaPket"), #OK
    path('error/', Tuerror, name="Tuerror"), #OK
    path('versolucion/<str:libro>/<str:numero>', versolucion,name='versolucion'), #OK


    path('login/', Milogin, name="Milogin"), #OK
    path('logout/', logout, name="logout"), #OK
    path('registrarse/', registro, name="registro"), #OK
    path('', index, name="index"), #OK
    path('ajax/compraPKT/', compraPKT, name='compraPKT'), #OK
    path('tematicas_actualizar/<slug:pk>', TematicasAct.as_view(),name='TematicasAct'), #OK
    path('tematicas_list', Tematicas.as_view(),name='listatemas'), #OK
    path('tematicas_form/', CreaTemas.as_view(), name='Createmas'), #OK
    path('borra_temas/<slug:pk>', BorraTemas.as_view(template_name='temas_confirm_delete.html'),name='borraTemas'), #OK
    path('libros_actualizar/<slug:pk>', librosAct.as_view(),name='librosAct'), #OK
    path('libros_list', ListaLibros.as_view(),name='listalibros'), #OK
    path('borra_libros/<slug:pk>', BorraLibro.as_view(template_name='libros_confirm_delete.html'),name='borralibros'), #OK
    path('libros_form/', CreaLibro.as_view(), name='CreaLibro'), #OK
    path('ajax/getProblemas/', getProblemas, name='getProblemas'),
    path('ajax/enviacorreoValidar/', enviacorreoValidar, name='enviacorreoValidar'),
    path('verPaquetes/<str:codigo>', verPaquetes,name="verPaquetes"), #OK
    path('busquedas/', consultar,name="consultar"), #OK
    path('verMiPKT/<str:pkt>', mipkt,name="mipkt"), #OK
    path('ajax/borraPa/', borraPa, name='borraPa'),
    path('ajax/poblarPaquetes/', poblarPaquetes, name='poblarPaquetes'),
    path('ajax/borrarPaquetes/', borrarPaquetes, name='borrarPaquetes'),
    path('ajax/getPaquetes/', getPaquetes, name='getPaquetes'),
    path('ajax/BuscaTemasxLibros/', BuscaTemasxLibros, name='BuscaTemasxLibros'),
    path('ajax/BuscaProblemas/', BuscaProblemas, name='BuscaProblemas'),
    path('ajax/Muestraproblemas/', Muestraproblemas, name='Muestraproblemas'),
    path('ajax/getDetalles/', getDetalles, name='getDetalles'),
    path('ajax/TranferMovil/', TranferMovil, name='TranferMovil'),
    path('TranferMovil/<str:pkt>/<str:usuario>', TranferMovil, name='TranferMovil'),
    path('contactanos/', contactanos,name="contactanos"),
    path('terminos/', terminos, name="terminos"),
    path('team/', team,name="team"),
    path('ajax/creaCodigo/', Creacodigo, name='Creacodigo'),
    path('promociones/', promociones,name="promociones"),
    path('listaPaquetes/<str:miperfil>', LPaquetes, name='LPaquetes') #OK
    ]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

