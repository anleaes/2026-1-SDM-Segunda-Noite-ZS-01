from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'generos'
router = routers.SimpleRouter()
router.register('', views.GeneroViewSet, basename='generos')

urlpatterns = [
    path('', include(router.urls))
]