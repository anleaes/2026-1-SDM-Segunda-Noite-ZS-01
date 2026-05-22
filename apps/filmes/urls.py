from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'filmes'
router = routers.SimpleRouter()
router.register('', views.FilmeViewSet, basename='filmes')

urlpatterns = [
    path('', include(router.urls))
]