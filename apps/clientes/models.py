from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Cliente(Usuario):
    telefone = models.CharField('Telefone', max_length=20)
    data_cadastro = models.DateTimeField('Data de cadastro', auto_now_add=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.nome