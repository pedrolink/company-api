from django.db import models
from empresas.models import Empresa
from usuarios.models import Usuario

class Plataforma(models.Model):
    funcionario = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)
    id_empresas = models.ManyToManyField(Empresa)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.funcionario

