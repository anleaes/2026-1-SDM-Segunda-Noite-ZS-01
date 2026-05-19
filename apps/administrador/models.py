from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Administrador(Usuario):
    nivel_acesso = models.CharField('Nível Acesso', max_length=2)
    matricula = models.DateTimeField('Matrícula', auto_now_add=True)

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administrador'
        ordering =['id']

    def __str__(self):
        return super().__str__()