from django.db import models
from empresas.models import Empresa

class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
    empresa = models.ManyToManyField(Empresa)

    def __str__(self):
        return self.usuario