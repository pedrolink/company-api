from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18)

    def __str__(self):
        return self.nome
