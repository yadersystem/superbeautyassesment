from django.db import models
from django.contrib.auth.models import User


class Equipo(models.Model):
    """
    It refers to the equipment model that will house its characteristics.
    """
    referencia = models.CharField(max_length=200)
    marca = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    memoria = models.IntegerField(max_length=100)
    disco = models.IntegerField(max_length=100)
    tipo = models.CharField(max_length=200)
    created_at = models.DateTimeField(False, True, editable=False)
    updated_at = models.DateTimeField(True, True, editable=False)


class EquipoUsuario(models.Model):
    """
    User to whom the team is assigned
    """
    equipo = models.ForeignKey(Equipo)
    usuario = models.ForeignKey(User, blank=True, null=True)
    fechaasignacion = models.DateField(null=False, max_length=50)
    fechaentrega = models.DateField(null=False, max_length=50)
