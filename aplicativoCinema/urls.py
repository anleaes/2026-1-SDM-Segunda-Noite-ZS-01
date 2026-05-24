"""
URL configuration for aplicativoCinema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('clientes/', include('clientes.urls', namespace='clientes')),
    path('administrador/', include('administrador.urls', namespace='administrador')),
    path('salas/', include('salas.urls', namespace='salas')),
    path('filmes/', include('filmes.urls', namespace='filmes')),
    path('pedido/', include('pedido.urls', namespace='pedido')),
    path('sessoes/', include('sessoes.urls', namespace='sessoes')),
    path('assentos/', include('assentos.urls', namespace='assentos')),
    path('pagamento/', include('pagamento.urls', namespace='pagamento')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)