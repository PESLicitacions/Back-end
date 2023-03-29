from django.urls import path
from . import views


urlpatterns = [
    path('licitacions_publiques', views.licitacions_publiques.as_view()),
    path('licitacions_publiques/<int:pk>/', views.licitacio_publica_detail.as_view()),
    path('licitacions_privades', views.licitacions_privades.as_view()),
    path('licitacions_privades/<int:pk>/', views.licitacio_privada_detail.as_view())
]