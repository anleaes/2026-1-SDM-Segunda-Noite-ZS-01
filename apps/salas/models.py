from django.db import models

# Create your models here.
class Sala(models.Model):
    numero = models.IntegerField('Número da Sala', unique=True)
    capacidade = models.IntegerField('Capacidade')
    sala3D = models.BooleanField('Sala 3D', default=False)

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'

    def verificarDisponibilidade(self):
        return True

    def __str__(self):
        return f"Sala {self.numero}"