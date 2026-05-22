from django.db import models
from generos.models import Genero
# Create your models here.
class Filme(models.Model):
    titulo = models.CharField('Título', max_length=200)
    duracao = models.IntegerField('Duração (min)')
    classificacao = models.CharField('Classificação', max_length=50)
    cartaz = models.ImageField('Cartaz', upload_to='cartazes/', null=True, blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

    def exibirDetalhes(self):
        return f"{self.titulo} - {self.duracao} min"

    def __str__(self):
        return self.titulo