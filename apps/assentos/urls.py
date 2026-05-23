from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'assentos'

router = DefaultRouter()
router.register(r'assentos', views.AssentoViewSet)

urlpatterns = [
    path('assentos/listar', views.listar_assentos, name='listar_assentos'),
    path('assentos/criar', views.criar_assento, name='criar_assento'),
    path('assentos/<int:id>/mudar-status/', views.mudar_status, name='mudar_status'),
    path('', include(router.urls)),
]