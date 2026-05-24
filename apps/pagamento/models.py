from django.db import models
from pedido.models import Pedido

# Create your models here.



class Pagamento(models.Model):
    METODO_CHOICES = [
        ('dinheiro', 'Dinheiro'),
        ('cartao_credito', 'Cartão de Crédito'),
        ('cartao_debito', 'Cartão de Débito'),
        ('pix', 'Pix'),
    ]

    pedido = models.OneToOneField(
        Pedido,
        on_delete=models.CASCADE,
        related_name='pagamento'
    )

    valor_total = models.DecimalField(
        'Valor total',
        max_digits=10,
        decimal_places=2
    )

    metodo = models.CharField(
        'Método de pagamento',
        max_length=30,
        choices=METODO_CHOICES
    )

    data_hora = models.DateTimeField(
        'Data e hora',
        auto_now_add=True
    )

    def processar(self):
        return True

    def estornar(self):
        pass

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['id']

    def __str__(self):
        return f'Pagamento do pedido {self.pedido.id}'