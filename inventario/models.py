from django.db import models
from django.contrib.auth.models import User


class Equipo(models.Model):
    """
    It refers to the equipment model that will house its characteristics.
    """
    referencia = models.TextField(max_length=200)
    marca = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    memoria = models.IntegerField()
    disco = models.IntegerField()
    tipo = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.marca


class EquipoUsuario(models.Model):
    """
    User to whom the team is assigned
    """
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    fechaasignacion = models.DateField(null=False, max_length=50)
    fechaentrega = models.DateField(null=False, max_length=50)
