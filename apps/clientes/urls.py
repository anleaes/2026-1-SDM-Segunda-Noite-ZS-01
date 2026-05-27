from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'clientes'

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('filmes/', views.listar_filmes, name='listar_filmes'),
    path('escolher/', views.escolher_sessao, name='escolher_sessao'),
    path('escolher/<int:filme_id>/', views.escolher_sessao, name='escolher_sessao_filme'),
    path('comprar/<int:sessao_id>/', views.comprar_ingresso, name='comprar_ingresso'),
    path('', include(router.urls)),
]