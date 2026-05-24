from django.db import models
from pedido.models import Pedido

# Create your models here.
class Ingresso(models.Model):
    STATUS_CHOICES = [
        ('criado', 'Criado'),
        ('validado', 'Validado'),
        ('cancelado', 'Cancelado'),
    ]

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='ingressos',
        verbose_name='Pedido'
    )

    idSessao = models.IntegerField(
        verbose_name='ID Sessão'
    )

    idAssento = models.IntegerField(
        verbose_name='ID Assento'
    )

    codigoPR = models.CharField(
        max_length=100,
        verbose_name='Código PR'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='criado',
        verbose_name='Status'
    )

    ingressoMeiaEntrada = models.BooleanField(
        default=False,
        verbose_name='Ingresso Meia Entrada'
    )

    def validar(self):
        self.status = 'validado'
        self.save()
        return True

    def __str__(self):
        return f'Ingresso {self.id} - Pedido {self.pedido_id} - {self.status}'

    class Meta:
        verbose_name = 'Ingresso'
        verbose_name_plural = 'Ingressos'