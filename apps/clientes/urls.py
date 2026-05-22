from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'clientes'

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('', include(router.urls)),
]