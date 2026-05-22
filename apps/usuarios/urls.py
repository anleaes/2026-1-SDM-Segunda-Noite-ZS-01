from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'usuarios'

router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)

urlpatterns = [
    path('login/',  views.login,  name='login'),
    path('logout/', views.logout, name='logout'),
    path('', include(router.urls)),
]