from django.urls import path
from ..core import views

app_name = 'pedido'

urlpatterns = [
    path('', views.listar_pedidos, name='lista'),
    path('<int:pedido_id>/', views.detalhe_pedido, name='detalhe'),
]