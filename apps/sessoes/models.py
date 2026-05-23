from django.db import models
from filmes.models import Filme
from salas.models import Sala

# REMOVA ESTA LINHA: 
# from django.contrib.auth.models import User 

# ADICIONE A IMPORTAÇÃO DA SUA CLASSE:
from administrador.models import Administrador 

class Sessao(models.Model):
    horario = models.DateTimeField('Horário da Sessão')
    ativa = models.BooleanField('Ativa', default=True)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name='sessoes')
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='sessoes')
    
    admin = models.ForeignKey(Administrador, on_delete=models.PROTECT, verbose_name='Administrador')

    class Meta:
        verbose_name = 'Sessão'
        verbose_name_plural = 'Sessões'

    def exibirDetalhes(self):
        return f"Sessão de {self.filme.titulo} na Sala {self.sala.numero}"

    def __str__(self):
        return f"{self.filme.titulo} - {self.horario.strftime('%d/%m/%Y %H:%M')}"