import hashlib

from django.shortcuts import render, redirect
from clientes.models import Cliente
from administrador.models import Administrador
from .models import Usuario
from .serializer import UsuarioSerializer
from rest_framework import viewsets


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


def _tipo_usuario(usuario):
    return 'administrador' if isinstance(usuario, Administrador) else 'cliente'


def _gerar_token(usuario):
    texto = f"{usuario.email}:{usuario.id}:{_tipo_usuario(usuario)}:{usuario.nome}"
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()


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
            request.session.update({
                'usuario_id': usuario.id,
                'usuario_nome': usuario.nome,
                'usuario_email': usuario.email,
                'usuario_tipo': _tipo_usuario(usuario),
                'token': _gerar_token(usuario),
            })
            return redirect('core:home')

        return render(request, template_name, {'erro': 'Senha incorreta'})

    return render(request, template_name)


def logout(request):
    request.session.flush()
    return redirect('usuarios:login')