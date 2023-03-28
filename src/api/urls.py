from django.urls import path
from . import views


urlpatterns = [
    path('new_api/licitacions_publiques', views.licitacions_publiques_preview),
    path('new_api/licitacio_publica_details', views.licitacio_publica_detail),
    path('new_api/licitacions_privades', views.licitacions_privades_preview),
    path('new_api/licitacio_privada_details', views.licitacio_privada_detail)
]