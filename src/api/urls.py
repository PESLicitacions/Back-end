from django.urls import path
from api.views import *
from users.views import *
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from publicdata.views import get_data
from users.views import edit_perfil
from licitacions.views import unfollow_licitacio, toggle_notification
from users.views import edit_perfil, login_view

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('licitacions', LicitacionsList.as_view()),
    path('licitacions/publiques', LicitacionsPubliquesList.as_view()),
    path('licitacions/privades', LicitacionsPrivadesList.as_view()),
    path('licitacions/favorites', LicitacionsFavoritesList.as_view()),
    path('licitacions/seguides', LicitacionsSeguidesList.as_view()),
    path('licitacions/following', LicitacionsFollowingList.as_view()),
    path('licitacions/<int:pk>/', LicitacioDetailView.as_view()),
    path('licitacions/<int:pk>/add-to-favorites', Add_to_favorites.as_view()),
    path('licitacions/<int:pk>/seguir', Seguir.as_view()),
    path('localitzacions', LocalitzacionsInfo.as_view()),
    path('ambits', AmbitsInfo.as_view()),
    path('departaments', DepartamentsInfo.as_view()),
    path('organs', OrgansInfo.as_view()),
    path('tipus_contracte', TipusContracteInfo.as_view()),
    path('login/', obtain_auth_token),
    path('delete/', delete_user),
    path('users/<int:pk>', UserDetailView.as_view()),
    path('users/<int:pk>/follow', follow.as_view()),
    path('users/following', ListFollowing.as_view()),
    path('users/followers', ListFollowers.as_view()),
    path('tipus_contracte/<int:pk>/add-to-preferences', add_to_preferences),
    path('editProfile/<str:cif>/', edit_perfil, name='edit_profile'),
    path('updateBD/', get_data, name='update_BD'),
    path('unfollow/<int:pk>', unfollow_licitacio, name='unfollow_licitacio'),
    path('notifications/<int:pk>', toggle_notification, name='toggle_notification'),
    path('login-user/', login_view, name='login_view'),
] + router.urls
