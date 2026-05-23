from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Assento
from .serializer import AssentoSerializer

# Create your views here.
class AssentoViewSet(viewsets.ModelViewSet):
    queryset = Assento.objects.all()
    serializer_class = AssentoSerializer

def listar_assentos(request):
    assentos = Assento.objects.all()
    return render(request, 'assentos/listar.html', {'assentos': assentos})

def mudar_status(request, id):
    assento = get_object_or_404(Assento, id=id)
    
    if request.method == 'POST':
        assento.status = not assento.status
        assento.save()
        return redirect('assentos:listar_assentos')
    
    return render(request, 'assentos/mudar_status.html', {'assento': assento})