from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Pedido


def listar_pedidos(request):
    pedidos = list(Pedido.objects.values('id', 'status', 'dataHora'))
    return JsonResponse(pedidos, safe=False)


def detalhe_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return JsonResponse({'id': pedido.id, 'status': pedido.status, 'dataHora': pedido.dataHora})