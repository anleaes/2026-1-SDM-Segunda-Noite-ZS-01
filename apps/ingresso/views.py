from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets

from .models import Ingresso
from .serializer import IngressoSerializer


class IngressoViewSet(viewsets.ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer


def listar_ingressos(request):
    ingressos = list(
        Ingresso.objects.values(
            'id',
            'pedido_id',
            'sessao_id',
            'assento_id',
            'codigoQR',
            'status',
            'ingressoMeiaEntrada'
        )
    )

    return JsonResponse(ingressos, safe=False)


def detalhe_ingresso(request, ingresso_id):
    ingresso = get_object_or_404(Ingresso, id=ingresso_id)

    return JsonResponse({
        'id': ingresso.id,
        'pedido': ingresso.pedido_id,
        'sessao': ingresso.sessao_id,
        'assento': ingresso.assento_id,
        'codigoQR': ingresso.codigoQR,
        'status': ingresso.status,
        'ingressoMeiaEntrada': ingresso.ingressoMeiaEntrada
    })


def validar_ingresso(request, ingresso_id):
    ingresso = get_object_or_404(Ingresso, id=ingresso_id)
    resultado = ingresso.validar()

    return JsonResponse({
        'validado': resultado,
        'id': ingresso.id,
        'status': ingresso.status
    })