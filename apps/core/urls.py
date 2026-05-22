from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.listar_pedidos, name='listar_pedidos'),
    path('<int:pedido_id>/', views.detalhe_pedido, name='detalhe_pedido'),
]