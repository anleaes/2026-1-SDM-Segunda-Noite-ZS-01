from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets

from .models import Ingresso
from .serializer import IngressoSerializer

# Create your views here.
