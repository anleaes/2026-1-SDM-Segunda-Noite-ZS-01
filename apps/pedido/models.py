from django.db import models


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('criado', 'Criado'),
        ('cancelado', 'Cancelado'),
        ('finalizado', 'Finalizado'),
    ]

    cliente = models.ForeignKey(
        'clientes.Cliente',
        on_delete=models.CASCADE,
        verbose_name='Cliente'
    )

    dataHora = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data e Hora'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='criado',
        verbose_name='Status'
    )

    def criarPedido(self):
        self.status = 'criado'
        self.save()

    def cancelarPedido(self):
        self.status = 'cancelado'
        self.save()

    def __str__(self):
        return f'Pedido {self.id} - Cliente {self.cliente_id} - {self.status}'

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'