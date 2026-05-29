from django.shortcuts import render


def home(request):
    usuario_tipo = request.session.get('usuario_tipo', 'visitante')
    template_name = 'core/home.html'
    context = {
        'usuario_tipo': usuario_tipo,
        'usuario_nome': request.session.get('usuario_nome'),
        'token': request.session.get('token'),
    }
    return render(request, template_name, context)