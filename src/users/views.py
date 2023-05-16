from rest_framework import generics
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import json
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

from users.serializers import *
from users.permissions import IsCreationOrIsAuthenticated
from users.models import *
from rest_framework.decorators import authentication_classes, permission_classes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from users.serializers import UserPreviewSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsCreationOrIsAuthenticated,)

class follow(APIView):
    authentication_classes(IsAuthenticated,)
    permission_classes(TokenAuthentication,)
    
    def post(self,request, pk):
        User = get_user_model()
        follower = request.user
        following = get_object_or_404(User, pk=pk)
        follows = Follow.objects.filter(follower=follower, following=following).first()
        if follows:
            follows.delete()
            response_data = {'following': following.email, 'user': follower.email, 'action': 'unfollowed', 'success': True}
        else:
            follows = Follow(follower=follower, following=following)
            follows.save()
            response_data = {'following': following.email, 'user': follower.email, 'action': 'followed', 'success': True}
        return JsonResponse(response_data)
    

class ListFollowing(generics.ListAPIView):
    authentication_classes(IsAuthenticated,)
    permission_classes(TokenAuthentication,)
    serializer_class = UserPreviewSerializer

    def get_queryset(self):
        user = self.request.user
        following = Follow.objects.filter(follower=user).values_list('following_id', flat=True)
        User = get_user_model()
        return User.objects.filter(id__in=following)
    

class ListFollowers(generics.ListAPIView):
    authentication_classes(IsAuthenticated,)
    permission_classes(TokenAuthentication,)
    serializer_class = UserPreviewSerializer

    def get_queryset(self):
        user = self.request.user
        followers = Follow.objects.filter(following=user).values_list('follower_id', flat=True)
        User = get_user_model()
        return User.objects.filter(id__in=followers)

    
@api_view(['PUT', 'GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def edit_perfil(request):
    try:
        perfil = CustomUser.objects.get(username = request.user.username)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PerfilSerializer(perfil, data=request.data, partial= True)
    if request.method == 'GET':
        serializer = PerfilSerializer(perfil)
        return Response(serializer.data)
    if request.method == 'PUT':
        data_cif = json.dumps(request.data.get('CIF')).strip('"').strip()
        if (len(data_cif) == 9 and not data_cif[0].isnumeric() and not data_cif[8].isnumeric() and data_cif[1:7].isnumeric()):
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                print(serializer.error_messages)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'El valor del nuevo CIF introducido es incorrecto'} , status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def login_view(request):
    if request.user.is_authenticated:
        return JsonResponse({'success': True})

    email = request.data.get('email')
    password = request.data.get('password')

    if not (email and password):
        return JsonResponse({'success': False, 'message': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({'success': True})
    else:
        print(f"Authentication failed for email: {email}")
        return JsonResponse({'success': False, 'message': 'Email or password incorrect.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def logout_view(request):
    logout(request)
    return Response({'success': True, 'message': 'Logout completed'})



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete_user(request):
    try:
        user = request.user
    except user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        user.delete()
        return Response({'success': True, 'message': 'Account deleted'})
