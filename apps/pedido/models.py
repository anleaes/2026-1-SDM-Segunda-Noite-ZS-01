from django.db import models

# Create your models here.

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('criado', 'Criado'),
        ('cancelado', 'Cancelado'),
        ('finalizado', 'Finalizado'),
    ]

    dataHora = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='criado'
    )

    def criarPedido(self):
        self.status = 'criado'
        self.save()

    def cancelarPedido(self):
        self.status = 'cancelado'
        self.save()

    def __str__(self):
        return f'Pedido {self.id} - {self.status}'