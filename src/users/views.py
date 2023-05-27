from rest_framework import generics
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes, api_view, action
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import json
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import views
from rest_framework import mixins
from rest_framework import generics

from licitacions.models import *
from users.serializers import *
from users.permissions import IsCreationOrIsAuthenticated
from users.models import *

from users.serializers import *

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsCreationOrIsAuthenticated,)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        if self.action == 'list':
            return UserPreviewSerializer
        if self.action == ('put' or 'delete') :
            return UserProfileSerializer
        return UserSerializer
    
    
    @action(methods=['put'], detail=False)
    def put(self, request, format=None):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    @action(methods=['delete'], detail=False)
    def delete(self, request, format=None):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserDetail(APIView):
    User = get_user_model()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsCreationOrIsAuthenticated,)
    """
    List all the users
    """
    def get(self, request, username, format=None):
        user = get_object_or_404(User, username=username)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    
    


class Follow(APIView):
    authentication_classes(IsAuthenticated,)
    permission_classes(TokenAuthentication,)
    
    def post(self,request, pk):
        User = get_user_model()
        follower = request.user
        following = get_object_or_404(User, id=pk)
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


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserPreviewSerializer
    queryset = CustomUser.objects.all()
   
    
class Add_to_preferences(APIView):
    authentication_classes(IsAuthenticated,)
    permission_classes(TokenAuthentication,)

    def post(self, request):
        user = request.user

        tipus_contracte_ids = request.query_params.get('tipus_contracte')
        PreferenceTipusContracte.objects.filter(user=user).delete()
        if tipus_contracte_ids is not None and tipus_contracte_ids != "":
            tipus_contracte_ids = [int(id) for id in tipus_contracte_ids.split(',')]
            for tipus_contracte_id in tipus_contracte_ids:
                tipus_contracte = get_object_or_404(TipusContracte, id=tipus_contracte_id)
                preference_tp = PreferenceTipusContracte(user=user, tipus_contracte=tipus_contracte)
                try:
                    preference_tp.save()
                except:
                    pass

        ambit_ids = request.query_params.get('ambit')
        PreferenceAmbit.objects.filter(user=user).delete()
        if ambit_ids is not None and ambit_ids != "":
            ambit_ids = [int(id) for id in ambit_ids.split(',')]
            for ambit_id in ambit_ids:
                ambit = get_object_or_404(Ambit, codi=ambit_id)
                preference_amb = PreferenceAmbit(user=user, ambit=ambit)
                try:
                    preference_amb.save()
                except:
                    pass
        
        pressupost_min = request.query_params.get('pressupost_min')
        pressupost_max = request.query_params.get('pressupost_max')
        PreferencePressupost.objects.filter(user=user).delete()
        if pressupost_min is not None or pressupost_max is not None:
            preference_press = PreferencePressupost(user=user, pressupost_min=pressupost_min, pressupost_max=pressupost_max)
            try:
                preference_press.save()
            except:
                pass
        
        privades = request.query_params.get('privades')
        print(privades)
        publiques = request.query_params.get('publiques')
        print(publiques)
        PreferenceTipusLicitacio.objects.filter(user=user).delete()
        if privades is not None or publiques is not None:
            if privades is None:
                privades = False
            if publiques is None:
                publiques = False
            preference_tipus_lic = PreferenceTipusLicitacio(user=user, privades=privades, publiques=publiques)
            try:
                preference_tipus_lic.save()
            except:
                pass

        return JsonResponse({'status': 'ok'})
    
    def get(self, request):
        user = request.user

        tipus_contracte_preferences = PreferenceTipusContracte.objects.filter(user=user)
        tipus_contracte_data = [{"id": p.tipus_contracte.id, "name": str(p.tipus_contracte)} for p in tipus_contracte_preferences]

        ambit_preferences = PreferenceAmbit.objects.filter(user=user)
        ambit_data = [{"id": p.ambit.codi, "name": p.ambit.nom} for p in ambit_preferences]

        pressupost_preference = PreferencePressupost.objects.filter(user=user).first()
        pressupost_data = {"pressupost_min": pressupost_preference.pressupost_min if pressupost_preference else None,
                           "pressupost_max": pressupost_preference.pressupost_max if pressupost_preference else None}

        tipus_lic_preference = PreferenceTipusLicitacio.objects.filter(user=user).first()
        tipus_lic_data = {"privades": tipus_lic_preference.privades if tipus_lic_preference else False,
                          "publiques": tipus_lic_preference.publiques if tipus_lic_preference else False}

        return JsonResponse({"tipus_contracte": tipus_contracte_data,
                             "ambit": ambit_data,
                             "pressupost": pressupost_data,
                             "tipus_licitacio": tipus_lic_data})
        
class RatingCreateView(APIView):
    def post(self, request):
        evaluating_user = request.POST.get('evaluating_user')
        evaluated_user = request.POST.get('evaluated_user')
        value = request.POST.get('value')

        user_from = get_object_or_404(CustomUser, email=evaluating_user)
        user_to = get_object_or_404(CustomUser, email=evaluated_user)

        rating = Rating(evaluating_user=user_from, evaluated_user=user_to, value=value)
        rating.save()

        return JsonResponse({'success': True})
