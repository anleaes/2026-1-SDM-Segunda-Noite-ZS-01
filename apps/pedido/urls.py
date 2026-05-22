from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'pedido'

router = DefaultRouter()
router.register(r'api', views.PedidoViewSet)

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),

    path('', include(router.urls)),
]