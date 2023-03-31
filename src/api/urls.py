from django.urls import path
from . import views


urlpatterns = [
    path('licitacions_publiques', views.LicitacionsPubliquesList.as_view()),
    path('licitacions_publiques/<int:pk>/', views.LicitacioPublicaDetail.as_view()),
    path('licitacions_privades', views.LicitacionsPrivadesList.as_view()),
    path('licitacions_privades/<int:pk>/', views.LicitacioPrivadaDetail.as_view()),
    path('localitzacions', views.LocalitzacionsInfo.as_view()),
    path('ambits', views.AmbitsInfo.as_view()),
    path('departaments', views.DepartamentsInfo.as_view()),
    path('organs', views.OrgansInfo.as_view()),
    path('tipus_contracte', views.TipusContracteInfo.as_view())
]