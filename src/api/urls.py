from django.urls import path
from api.views import *
from users.views import UserViewSet
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from publicdata.views import get_data
from users.views import edit_perfil

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('licitacions', LicitacionsList.as_view()),
    path('licitacions/publiques', LicitacionsPubliquesList.as_view()),
    path('licitacions/privades', LicitacionsPrivadesList.as_view()),
    path('licitacions/favorites', LicitacionsFavoritesList.as_view()),
    path('licitacions/follow', LicitacionsFollowList.as_view()),
    path('licitacions/<int:pk>/', LicitacioDetailView.as_view()),
    path('licitacions/<int:pk>/add-to-favorites', Add_to_favorites.as_view()),
    path('licitacions/<int:pk>/add-to-follow', Add_to_follow.as_view()),
    path('localitzacions', LocalitzacionsInfo.as_view()),
    path('ambits', AmbitsInfo.as_view()),
    path('departaments', DepartamentsInfo.as_view()),
    path('organs', OrgansInfo.as_view()),
    path('tipus_contracte', TipusContracteInfo.as_view()),
    path('login/', obtain_auth_token),
    path('tipus_contracte/<int:pk>/add-to-preferences', add_to_preferences),
    path('editProfile/<str:cif>/', edit_perfil, name='edit_profile'),
    path('updateBD/', get_data, name='update_BD'),
] + router.urls
