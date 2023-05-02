from django.urls import path
from . import views
from users.views import register_view, login_view, edit_perfil


urlpatterns = [
    path('licitacions', views.LicitacionsList.as_view()),
    path('licitacions/<int:pk>/', views.LicitacioDetailView.as_view()),
    path('licitacions/publiques', views.LicitacionsPubliquesList.as_view()),
    path('licitacions/privades', views.LicitacionsPrivadesList.as_view()),
    path('localitzacions', views.LocalitzacionsInfo.as_view()),
    path('ambits', views.AmbitsInfo.as_view()),
    path('departaments', views.DepartamentsInfo.as_view()),
    path('organs', views.OrgansInfo.as_view()),
    path('tipus_contracte', views.TipusContracteInfo.as_view()),
    path('register/', register_view, name='register'), 
    path('login/', login_view, name='login'),
    path('editProfile/<str:cif>/', edit_perfil, name='edit_profile'),

]