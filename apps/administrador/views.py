from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import Administrador
from .serializer import AdministradorSerializer

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

def cadastrar(request):
    template_name = 'admin/cadastrar.html'
    if request.method == 'POST':
        Administrador.objects.create(
            nome=request.POST.get('nome'),
            cpf=request.POST.get('cpf'),
            email=request.POST.get('email'),
            senha=request.POST.get('senha'),
            nivel_acesso=request.POST.get('nivel_acesso'),
            matricula=request.POST.get('matricula'),
        )
        return redirect('usuarios:login')
    return render(request, template_name)