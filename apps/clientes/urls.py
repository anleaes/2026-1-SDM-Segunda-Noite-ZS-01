from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'clientes'

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
]