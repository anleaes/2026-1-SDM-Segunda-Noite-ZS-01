from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializer import ClientesSerializer
# Create your views here.
class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer  
