from django.shortcuts import render
from django.http import HttpResponse
from .models import Pedido

# Create your views here.
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido/listar.html', {'pedidos': pedidos})


def detalhe_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    return HttpResponse(f'Pedido {pedido.id} - Status: {pedido.status}')