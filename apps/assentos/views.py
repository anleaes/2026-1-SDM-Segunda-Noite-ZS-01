from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden 
from rest_framework import viewsets, permissions 
from .models import Assento
from .serializer import AssentoSerializer
from salas.models import Sala

# Create your views here.
class AssentoViewSet(viewsets.ModelViewSet):
    queryset = Assento.objects.all()
    serializer_class = AssentoSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

def listar_assentos(request):
    assentos = Assento.objects.all()
    return render(request, 'assentos/listar.html', {'assentos': assentos})

def criar_assento(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Acesso Negado: Apenas a administração pode criar assentos.")

    if request.method == 'POST':
        id_sala = request.POST.get('id_sala')
        fila = request.POST.get('fila')
        numero = request.POST.get('numero')
        status = request.POST.get('status') == 'true'

        Assento.objects.create(
            id_sala_id=id_sala,
            fila=fila,
            numero=numero,
            status=status
        )
        return redirect('assentos:listar_assentos')

    salas = Sala.objects.all()
    return render(request, 'assentos/criar_assento.html', {'salas': salas})

def mudar_status(request, id):
    assento = get_object_or_404(Assento, id=id)
    
    if request.method == 'POST':
        assento.status = not assento.status
        assento.save()
        return redirect('assentos:listar_assentos')
    
    return render(request, 'assentos/mudar_status.html', {'assento': assento})