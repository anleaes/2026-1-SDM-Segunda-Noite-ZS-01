from django.shortcuts import render, redirect
from .models import Cliente
from .serializer import ClientesSerializer
from rest_framework import viewsets
from sessoes.models import Sessao
from assentos.models import Assento
from pedido.models import Pedido
from filmes.models import Filme
from django.contrib import messages

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

def cadastrar(request):
    template_name = 'clientes/cadastrar.html'
    
    if request.method == 'POST':
        Cliente.objects.create(
            nome=request.POST.get('nome'),
            cpf=request.POST.get('cpf'),
            email=request.POST.get('email'),
            senha=request.POST.get('senha'),
            telefone=request.POST.get('telefone'),
        )
        return redirect('usuarios:login')
    
    return render(request, template_name)


def listar_filmes(request):
    filmes = Filme.objects.select_related('genero').all()
    return render(request, 'clientes/listar_filmes.html', {'filmes': filmes})


def escolher_sessao(request, filme_id=None):
    qs = Sessao.objects.select_related('filme', 'sala').filter(ativa=True)
    filme = None
    if filme_id:
        filme = Filme.objects.get(id=filme_id)
        qs = qs.filter(filme_id=filme_id)
    return render(request, 'clientes/escolher_sessao.html', {'sessoes': qs, 'filme': filme})


def comprar_ingresso(request, sessao_id):
    sessao = Sessao.objects.select_related('filme', 'sala').get(id=sessao_id)
    assentos = Assento.objects.filter(id_sala=sessao.sala).order_by('fila', 'numero')

    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        assento_id = request.POST.get('assento_id')

        cliente = None
        if cpf:
            try:
                cliente = Cliente.objects.get(cpf=cpf)
            except Cliente.DoesNotExist:
                cliente = None

        if not cliente:
            messages.error(request, 'Cliente não encontrado. Cadastre-se primeiro.')
            return redirect('clientes:cadastrar')

        pedido = Pedido.objects.create(cliente=cliente)

        try:
            assento = Assento.objects.get(id=assento_id, id_sala=sessao.sala)  # removido status=False
            if assento.status and assento.status != 0:  # já ocupado
                messages.error(request, 'Assento indisponível. Escolha outro.')
                return redirect('clientes:comprar_ingresso', sessao_id=sessao.id)
            assento.status = True
            assento.save()
        except Assento.DoesNotExist:
            messages.error(request, 'Assento não encontrado.')
            return redirect('clientes:comprar_ingresso', sessao_id=sessao.id)

        messages.success(request, f'Ingresso reservado: {assento.fila}{assento.numero} para {sessao.filme.titulo}.')
        return render(request, 'clientes/compra_confirmacao.html', {'pedido': pedido, 'sessao': sessao, 'assento': assento})

    return render(request, 'clientes/comprar_ingresso.html', {'sessao': sessao, 'assentos': assentos})