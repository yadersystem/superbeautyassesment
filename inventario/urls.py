from django.urls import path

from . import views

urlpatterns = [
    path('equipo/', views.equipo, name='equipo'),
    path('equipo_details/', views.equipo_details, name='equipo_details'),
    path('equipousuario/', views.equipousuario, name='equipousuario'),
    path('usuarios_details/', views.usuarios_details, name='usuarios_details'),
    path('', views.filtros, name='index'),
]