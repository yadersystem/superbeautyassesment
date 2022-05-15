from django.contrib import admin
from inventario.models import Equipo, EquipoUsuario
from django.db import models


class EquipoAdmin(admin.ModelAdmin):
    list_display = ('referencia', 'marca', 'procesador', 'memoria', 'disco', 'tipo', 'created_at', 'updated_at')
    search_fields = ('referencia',)


class EquipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'usuario', 'fechaasignacion', 'fechaentrega')
    search_fields = ('fechaasignacion', 'usuario')


admin.site.register(Equipo, EquipoAdmin)
admin.site.register(EquipoUsuario, EquipoUsuarioAdmin)
