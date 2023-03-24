from django.db import models


class Clientes(models.Model):
    Nome = models.CharField(max_length=20, null=False)
    CPF = models.CharField(max_length=11, null=False)
    Endereco = models.CharField(max_length=100, null=False)
    Cidade = models.CharField(max_length=10, null=False)
    Estado = models.CharField(max_length=6, null=False)

    def __str__(self) -> str:
        return self.Nome

