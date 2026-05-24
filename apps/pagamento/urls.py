from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'pagamento'

router = DefaultRouter()
router.register(r'api', views.PagamentoViewSet, basename='pagamento')

urlpatterns = [
    # adicona depois
]

urlpatterns += router.urls