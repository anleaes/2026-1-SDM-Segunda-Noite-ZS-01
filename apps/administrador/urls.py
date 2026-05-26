from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'administrador'

router = DefaultRouter()
router.register(r'administrador', views.AdministradorViewSet)

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
 
    path('filmes/', views.listar_filmes, name='listar_filmes'),
    path('filmes/cadastrar/', views.cadastrar_filme, name='cadastrar_filme'),
    path('filmes/<int:pk>/editar/', views.editar_filme, name='editar_filme'),
 
    path('sessoes/', views.listar_sessoes, name='listar_sessoes'),
    path('sessoes/cadastrar/', views.cadastrar_sessao, name='cadastrar_sessao'),
    path('sessoes/<int:pk>/editar/', views.editar_sessao, name='editar_sessao'),
    path('sessoes/<int:pk>/inativar/', views.inativar_sessao, name='inativar_sessao'),
 
    path('salas/', views.listar_salas, name='listar_salas'),
    path('salas/cadastrar/', views.cadastrar_sala, name='cadastrar_sala'),
    path('salas/<int:pk>/editar/', views.editar_sala, name='editar_sala'),
    path('salas/<int:pk>/inativar/', views.inativar_sala, name='inativar_sala'),
    path('salas/<int:sala_pk>/assentos/criar/', views.criar_assento, name='criar_assento'),
 
    path('', include(router.urls)),
]