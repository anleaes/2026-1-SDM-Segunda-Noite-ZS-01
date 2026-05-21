from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'usuarios'

urlpatterns = [
    path('login/',  views.login,  name='login'),
    path('logout/', views.logout, name='logout'),
]