from django.db import models


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('criado', 'Criado'),
        ('cancelado', 'Cancelado'),
        ('finalizado', 'Finalizado'),
    ]

    dataHora = models.DateTimeField(auto_now_add=True, verbose_name='Data e Hora')
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
        return f'Pedido {self.id} - {self.status}'

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ('PENDENTE', 'Pendente'),
        ('CRIADO', 'Criado'),
        ('CANCELADO', 'Cancelado'),
    ]

    data_hora = models.DateTimeField('Data e Hora', auto_now_add=True)
    status = models.CharField(
        'Status',
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDENTE'
    )

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']

    def criar_pedido(self):
        self.status = 'CRIADO'
        self.save()

    def cancelar_pedido(self):
        self.status = 'CANCELADO'
        self.save()

    def __str__(self):
        return f'Pedido {self.id} - {self.status}'
