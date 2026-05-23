from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'clientes'

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('escolher/', views.escolher_sessao, name='escolher_sessao'),
    path('comprar/<int:sessao_id>/', views.comprar_ingresso, name='comprar_ingresso'),
    path('', include(router.urls)),
]