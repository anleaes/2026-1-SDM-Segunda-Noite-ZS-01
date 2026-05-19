from django.shortcuts import render
from rest_framework import viewsets
from .models import Administrador
from .serializer import AdministradorSerializer
# Create your views here.
class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer  
