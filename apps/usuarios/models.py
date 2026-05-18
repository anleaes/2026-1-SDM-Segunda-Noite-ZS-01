from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome  = models.CharField('Nome', max_length=255)
    cpf   = models.CharField('CPF', max_length=14, unique=True)
    email = models.EmailField('Email', unique=True)
    senha = models.CharField('Senha', max_length=12, null=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering =['id']

    def __str__(self):
        return self.nome