from django.shortcuts import render
from .models import Filme
from rest_framework import viewsets
from .serializer import FilmeSerializer
# Create your views here.
class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer