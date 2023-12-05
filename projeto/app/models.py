from django.db import models

class Reserva(models.Model):
    cnpj = models.CharField(max_length=20)
    nome_empresa = models.CharField(max_length=200)
    quitado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_empresa

# Create your models here.
