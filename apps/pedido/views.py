from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets

from rest_framework import viewsets
from .models import Pedido

from .serializers import PedidoSerializer
from clientes.models import Cliente



def cadastrar(request):
    if request.method == 'POST':
        status = request.POST.get('status', 'criado')

        Pedido.objects.create(
            status=status
        )

        return redirect('pedido:cadastrar')

    return render(request, 'pedido/cadastrar.html')


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


def listar_pedidos(request):
    pedidos = list(Pedido.objects.values('id', 'status', 'dataHora'))
    return JsonResponse(pedidos, safe=False)


def detalhe_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    return JsonResponse({
        'id': pedido.id,
        'status': pedido.status,
        'dataHora': pedido.dataHora
    })
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
