from django.shortcuts import render, redirect
from clientes.models import Cliente
from administrador.models import Administrador
from .serializer import UsuarioSerializer
from rest_framework import viewsets

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = UsuarioSerializer

def login(request):
    template_name = 'usuarios/login.html'
    
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        usuario = None
        for Model in [Cliente, Administrador]:
            try:
                usuario = Model.objects.get(email=email)
                break
            except Model.DoesNotExist:
                continue
        
        if usuario is None:
            return render(request, template_name, {'erro': 'Usuário não encontrado'})
        
        if usuario.login(senha):
            request.session['usuario_id'] = usuario.id
            request.session['usuario_nome'] = usuario.nome
            return redirect('usuarios:home')
        
        return render(request, template_name, {'erro': 'Senha incorreta'})
    
    return render(request, template_name)

def logout(request):
    request.session.flush()
    return redirect('usuarios:login')