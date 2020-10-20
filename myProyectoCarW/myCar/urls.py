from django.contrib import admin
from django.urls import path, include
from .views import index, galeria,quien,login,cerrar_sesion,insumos,registro,lista_insumos,eliminar,busqueda_mod,modificar

urlpatterns = [
    path('',index,name='INDEX'),
    path('galeria/',galeria,name='GALE'),
    path('quienes/',quien,name='QUIEN'),
    path('login/',login, name='LOGIN'),
    path('cerrar_sesion/',cerrar_sesion,name='LOGOUT'),
    path('insumos/',insumos,name='INSUMOS'),
    path('registro/',registro,name='REGISTRO'),
    path('lista_insumos/',lista_insumos,name='LISTAINSUMO'),
    path('eliminar/<id>/',eliminar,name='ELIMINAR'),
    path('buscar/<id>/',busqueda_mod,name='BUSCAR'),
    path('modificar/',modificar,name='MODIFICAR'),
]