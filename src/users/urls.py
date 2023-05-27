from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from users.views import *

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # Post, Put, Delete, Get of the Own profile
    path('', UserViewSet.as_view({ "get": "list", "post": "create", "put": "put", "delete": "delete"})),
    path('<str:username>', UserDetail.as_view(), name='user-detail'),
    
    # Get the token
    path('login/', obtain_auth_token),
    
    # Get return preferences, Post create them, Put modifie them
    path('preferences', Add_to_preferences.as_view()),
    
    
    path('editProfile', edit_perfil, name='edit_profile'),
    
    path('delete/', delete_user),
    
    
    # User details, if Get of own user, return full details
    path('<int:pk>', UserDetailView.as_view()),
    
    # Post Follow a user if not following else unfollow
    path('<int:pk>/follow', Follow.as_view()),
    # Get users Following
    path('following', ListFollowing.as_view()),
    # Get userse that follow you
    path('followers', ListFollowers.as_view()),
    path('ratings/', RatingCreateView.as_view(), name='rating_create'),

    
    
    

] + router.urls
