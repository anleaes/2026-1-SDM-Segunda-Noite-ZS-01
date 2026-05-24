from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'ingresso'

router = DefaultRouter()
router.register(r'api', views.IngressoViewSet, basename='ingresso')

urlpatterns = [
    path('listar/', views.listar_ingressos, name='listar'),
    path('detalhe/<int:ingresso_id>/', views.detalhe_ingresso, name='detalhe'),
    path('validar/<int:ingresso_id>/', views.validar_ingresso, name='validar'),
]

urlpatterns += router.urls