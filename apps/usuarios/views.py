import hashlib

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
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


def _is_api_request(request):
    return 'application/json' in request.headers.get('Accept', '')


@csrf_exempt
def login(request):
    template_name = 'usuarios/login.html'
    is_api = _is_api_request(request)

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
            if is_api:
                return JsonResponse({'success': False, 'detail': 'Usuário não encontrado'}, status=400)
            return render(request, template_name, {'erro': 'Usuário não encontrado'})

        if usuario.login(senha):
            request.session.update({
                'usuario_id': usuario.id,
                'usuario_nome': usuario.nome,
                'usuario_email': usuario.email,
                'usuario_tipo': _tipo_usuario(usuario),
                'token': _gerar_token(usuario),
            })
            if is_api:
                return JsonResponse({
                    'success': True,
                    'token': request.session.get('token'),
                    'usuario': {
                        'id': usuario.id,
                        'nome': usuario.nome,
                        'tipo': _tipo_usuario(usuario),
                    },
                })
            return redirect('core:home')

        if is_api:
            return JsonResponse({'success': False, 'detail': 'Senha incorreta'}, status=400)
        return render(request, template_name, {'erro': 'Senha incorreta'})

    if is_api:
        return JsonResponse({'detail': 'Método não permitido'}, status=405)
    return render(request, template_name)


def logout(request):
    request.session.clear()
    return redirect('usuarios:login')