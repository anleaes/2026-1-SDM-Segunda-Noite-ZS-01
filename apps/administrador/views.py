from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import viewsets

from .models import Administrador
from .serializer import AdministradorSerializer

from filmes.models import Filme
from sessoes.models import Sessao
from salas.models import Sala
from assentos.models import Assento
from generos.models import Genero

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
        )
        return redirect('usuarios:login')
    return render(request, template_name)

def cadastrar_filme(request):
    template_name = 'admin/cadastrar_filme.html'
    generos = Genero.objects.all()

    if request.method == 'POST':
        Filme.objects.create(
            titulo=request.POST.get('titulo'),
            duracao=request.POST.get('duracao'),
            classificacao=request.POST.get('classificacao'),
            genero_id=request.POST.get('genero'),
            cartaz=request.FILES.get('cartaz')
        )

        messages.success(request, 'Filme cadastrado com sucesso!')
        return redirect('administrador:listar_filmes')

    return render(request, template_name, {
        'generos': generos
    })

def listar_filmes(request):
    filmes = Filme.objects.all().order_by('-id')
    return render(request, 'admin/listar_filme.html', {'filmes': filmes})


def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    generos = Genero.objects.all()

    template_name = 'admin/editar_filme.html'

    if request.method == 'POST':
        filme.titulo = request.POST.get('titulo')
        filme.duracao = request.POST.get('duracao')
        filme.classificacao = request.POST.get('classificacao')
        filme.genero_id = request.POST.get('genero')

        if request.FILES.get('cartaz'):
            filme.cartaz = request.FILES.get('cartaz')

        filme.save()

        messages.success(request, 'Filme atualizado com sucesso!')
        return redirect('administrador:listar_filmes')

    return render(request, template_name, {
        'filme': filme,
        'generos': generos
    })

def remover_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    if request.method == 'POST':
        titulo = filme.titulo

        filme.delete()

        messages.success(request, f'Filme "{titulo}" removido com sucesso!')

    return redirect('administrador:listar_filmes')


def listar_generos(request):
    generos = Genero.objects.all().order_by('nome')
    return render(request, 'admin/listar_genero.html', {'generos': generos})


def cadastrar_genero(request):
    template_name = 'admin/cadastrar_genero.html'
    if request.method == 'POST':
        Genero.objects.create(
            nome=request.POST.get('nome'),
            descricao=request.POST.get('descricao'),
            icone=request.POST.get('icone')
        )
        messages.success(request, 'Gênero cadastrado com sucesso!')
        return redirect('administrador:listar_generos')

    return render(request, template_name)


def editar_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    template_name = 'admin/editar_genero.html'

    if request.method == 'POST':
        genero.nome = request.POST.get('nome')
        genero.descricao = request.POST.get('descricao')
        genero.icone = request.POST.get('icone')
        genero.save()

        messages.success(request, 'Gênero atualizado com sucesso!')
        return redirect('administrador:listar_generos')

    return render(request, template_name, {'genero': genero})


def remover_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        nome = genero.nome
        genero.delete()
        messages.success(request, f'Gênero "{nome}" removido com sucesso!')

    return redirect('administrador:listar_generos')

def cadastrar_sessao(request):
    template_name = 'admin/cadastrar_sessao.html'

    salas = Sala.objects.all()
    filmes = Filme.objects.all()

    if request.method == 'POST':

        admin = Administrador.objects.first()

        Sessao.objects.create(
            horario=request.POST.get('horario'),
            ativa=True,
            filme_id=request.POST.get('filme'),
            sala_id=request.POST.get('sala'),
            admin=admin
        )

        messages.success(request, 'Sessão cadastrada com sucesso!')
        return redirect('administrador:listar_sessoes')

    return render(request, template_name, {
        'salas': salas,
        'filmes': filmes
    })

def listar_sessoes(request):
    sessoes = Sessao.objects.select_related(
        'filme',
        'sala',
        'admin'
    ).order_by('-horario')

    return render(request, 'admin/listar_sessao.html', {
        'sessoes': sessoes
    })

def inativar_sessao(request, pk):
    sessao = get_object_or_404(Sessao, pk=pk)

    if request.method == 'POST':
        sessao.ativa = False
        sessao.save()

        messages.success(request, 'Sessão inativada com sucesso!')

    return redirect('administrador:listar_sessoes')

def cadastrar_sala(request):
    template_name = 'admin/cadastrar_sala.html'
    if request.method == 'POST':
        Sala.objects.create(
            numero=request.POST.get('numero'),
            capacidade=request.POST.get('capacidade'),
            sala3D=request.POST.get('sala3D') == 'on'
        )
        messages.success(request, 'Sala cadastrada com sucesso!')
        return redirect('administrador:listar_salas')
    return render(request, template_name)

def listar_salas(request):
    salas = Sala.objects.all().order_by('numero')
    return render(request, 'admin/listar_sala.html', {'salas': salas})

def editar_sessao(request, pk):
    sessao = get_object_or_404(Sessao, pk=pk)

    filmes = Filme.objects.all()
    salas = Sala.objects.all()

    if request.method == 'POST':
        sessao.horario = request.POST.get('horario')
        sessao.filme_id = request.POST.get('filme')
        sessao.sala_id = request.POST.get('sala')

        sessao.save()

        messages.success(request, 'Sessão atualizada com sucesso!')
        return redirect('administrador:listar_sessoes')

    return render(request, 'admin/editar_sessao.html', {
        'sessao': sessao,
        'filmes': filmes,
        'salas': salas
    })

def inativar_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    if request.method == 'POST':
        has_sessoes = sala.sessoes.exists()
        has_ingressos_em_assentos = sala.assentos.filter(ingresso__isnull=False).exists()

        if has_sessoes or has_ingressos_em_assentos:
            messages.error(
                request,
                f'Não é possível remover a sala {sala.numero}: existem sessões ou assentos vinculados a ingressos.'
            )
        else:
            sala.delete()
            messages.success(request, f'Sala "{sala.numero}" removida.')
    return redirect('administrador:listar_salas')

def editar_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)

    template_name = 'admin/editar_sala.html'

    if request.method == 'POST':
        sala.numero = request.POST.get('numero')
        sala.capacidade = request.POST.get('capacidade')
        sala.sala3D = request.POST.get('sala3D') == 'on'

        sala.save()

        messages.success(request, 'Sala atualizada com sucesso!')
        return redirect('administrador:listar_salas')

    return render(request, template_name, {
        'sala': sala
    })
def criar_assento(request, sala_pk):
    sala = get_object_or_404(Sala, pk=sala_pk)

    if request.method == 'POST':

        fileiras = request.POST.get('fileiras', '').upper()
        colunas = int(request.POST.get('colunas', 0))

        assentos_criados = 0

        for letra in fileiras:
            for numero in range(1, colunas + 1):

                _, created = Assento.objects.get_or_create(
                    id_sala=sala,
                    fila=letra,
                    numero=numero
                )

                if created:
                    assentos_criados += 1

        messages.success(
            request,
            f'{assentos_criados} assento(s) criado(s) para a sala {sala.numero}.'
        )

        return redirect('administrador:listar_salas')

    return render(request, 'admin/criar_assento.html', {
        'sala': sala
    })

def inativar_assento(request, pk):
    assento = get_object_or_404(Assento, pk=pk)

    if request.method == 'POST':

        try:
            ingresso = assento.ingresso
        except Exception:
            ingresso = None

        if ingresso and ingresso.status != 'cancelado':
            messages.error(
                request,
                f'Não é possível inativar o assento {assento.fila}{assento.numero}: existe um ingresso ativo.'
            )
        else:
            assento.status = False
            assento.save()

            messages.success(
                request,
                f'Assento {assento.fila}{assento.numero} inativado com sucesso!'
            )

    return redirect('administrador:listar_salas')

def ativar_assento(request, pk):
    assento = get_object_or_404(Assento, pk=pk)

    if request.method == 'POST':

        assento.status = True
        assento.save()

        messages.success(
            request,
            f'Assento {assento.fila}{assento.numero} ativado com sucesso!'
        )

    return redirect('administrador:listar_salas')