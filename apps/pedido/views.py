from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from clientes.models import Cliente
from .models import Pedido
from .serializer import PedidoSerializer


def cadastrar(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        status = request.POST.get('status', 'criado')

        try:
            cliente = Cliente.objects.get(cpf=cpf)
        except Cliente.DoesNotExist:
            return render(request, 'pedido/cadastrar.html', {'erro': 'Cliente não encontrado'})

        Pedido.objects.create(cliente=cliente, status=status)
        return redirect('pedido:cadastrar')

    return render(request, 'pedido/cadastrar.html')


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    @action(detail=True, methods=['post'])
    def cancelar(self, request, pk=None):
        pedido = self.get_object()
        pedido.status = 'cancelado'
        pedido.save()
        return Response({'status': 'cancelado', 'id': pedido.id})

    @action(detail=True, methods=['post'])
    def criar(self, request, pk=None):
        pedido = self.get_object()
        pedido.status = 'criado'
        pedido.save()
        return Response({'status': 'criado', 'id': pedido.id})