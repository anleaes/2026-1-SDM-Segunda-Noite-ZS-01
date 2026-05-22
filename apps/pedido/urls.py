from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'pedido'

router = DefaultRouter()
router.register(r'api', views.PedidoViewSet, basename='pedido')

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
]

urlpatterns += router.urls