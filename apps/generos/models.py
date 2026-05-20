from django.db import models

# Create your models here.
class Genero(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição')
    icone = models.CharField('Ícone', max_length=255)

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'

    def __str__(self):
        return self.nome