from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'administrador'

router = routers.SimpleRouter()
router.register('', views.AdministradorViewSet, basename='administrador')

urlpatterns = [
    path('', include(router.urls) )
]