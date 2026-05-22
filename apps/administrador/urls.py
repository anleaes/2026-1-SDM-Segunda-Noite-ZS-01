from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'administrador'

router = DefaultRouter()
router.register(r'administrador', views.AdministradorViewSet)

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),

    path('', include(router.urls)),
]