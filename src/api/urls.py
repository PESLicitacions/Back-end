from django.urls import path
from . import views


urlpatterns = [
    path('licitacions_publiques', views.LicitacionsPubliquesList.as_view()),
    path('licitacions_publiques/<int:pk>/', views.LicitacioPublicaDetail.as_view()),
    path('licitacions_privades', views.LicitacionsPrivadesList.as_view()),
    path('licitacions_privades/<int:pk>/', views.LicitacioPrivadaDetail.as_view())
]