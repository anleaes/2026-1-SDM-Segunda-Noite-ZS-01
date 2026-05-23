from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Assento(models.Model):
    FILA_CHOICES = [
        ('A', 'Fila A'),
        ('B', 'Fila B'),
        ('C', 'Fila C'),
        ('D', 'Fila D'),
        ('E', 'Fila E'),
    ]

    id_sala = models.ForeignKey('salas.Sala', on_delete=models.CASCADE, related_name='assentos')
    fila = models.CharField(max_length=1, choices=FILA_CHOICES)
    numero = models.IntegerField(validators=[MinValueValidator(1)])
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Assento'
        verbose_name_plural = 'Assentos'
        unique_together = ('id_sala', 'fila', 'numero')

    def __str__(self):
        return f'Assento {self.fila}{self.numero} - Sala {self.id_sala}'
