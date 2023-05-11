from django.urls import path
from api.views import *
from users.views import *
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from publicdata.views import get_data
from users.views import edit_perfil
from users.views import edit_perfil, login_view, logout

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('licitacions', LicitacionsList.as_view()),
    path('licitacions/public', LicitacionsPubliquesList.as_view()),
    path('licitacions/private', LicitacionsPrivadesList.as_view()),
    path('licitacions/favorites', LicitacionsFavoritesList.as_view()),
    path('licitacions/following', LicitacionsSeguidesList.as_view()),
    path('licitacions/preferences', LicitacionsPreferencesList.as_view()),
    path('licitacions/<int:pk>/', LicitacioDetailView.as_view()),
    path('licitacions/<int:pk>/save', Add_to_favorites.as_view()),
    path('licitacions/<int:pk>/follow', Seguir.as_view()),
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
    path('users/following/licitacions', LicitacionsFollowingList.as_view()),
    path('users/followers', ListFollowers.as_view()),
    path('preferences', Add_to_preferences.as_view()),
    path('editProfile/<str:cif>/', edit_perfil, name='edit_profile'),
    path('updateBD/', get_data, name='update_BD'),
    path('login-user/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view')
] + router.urls
