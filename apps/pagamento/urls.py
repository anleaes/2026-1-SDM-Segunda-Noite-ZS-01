from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PagamentoViewSet

app_name = 'pagamento'

router = DefaultRouter()
router.register(r'pagamentos', PagamentoViewSet, basename='pagamento')

urlpatterns = [
    path('', include(router.urls)),
]