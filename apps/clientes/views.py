from django.shortcuts import render, redirect
from .models import Cliente

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