from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'salas'
router = routers.SimpleRouter()
router.register('', views.SalaViewSet, basename='salas')

urlpatterns = [
    path('', include(router.urls))
]