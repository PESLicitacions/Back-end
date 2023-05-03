'''
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import Perfil
from .serializers import PerfilSerializer
from rest_framework import status

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


# Create your views here
@csrf_exempt  
def login_view(request):
    if request.user.is_authenticated:
        return JsonResponse({'success': True})
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                content = {
                    'user': str(request.user),  # `django.contrib.auth.User` instance.
                    'auth': str(request.auth),  # None
                }
                response_data = {'success': True}
            else:
                response_data = {'success': False, 'message': 'Username or password incorrect'}
            return JsonResponse(content)
    
@csrf_exempt    
def register_view(request):
    if request.user.is_authenticated:
        print("SOC DINS IF")
        response_data = {'success': True, 'message': 'El usuario ya esta autentificado.'}
        return JsonResponse(response_data)
    else:
        print(request.method)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if request.method == 'POST':
            username = body.get('username')
            email = body.get('email')
            name = body.get('name')
            password = body.get('password')
            password2 = body.get('password2')
        
            customUs = CustomUser.objects.create(
                email = email,
                username = username,
                password = password,
                name = name,
            )
            
            token = Token.objects.create(user=customUs)
            
            print("Se ha creado el usuario con username: "+ customUs.username)
            response_data = {'success': True, 'message': 'El usuario se ha registrado correctamente.'}
            print(response_data)
            return JsonResponse(response_data)
        else: 
            print("HE entrar a l'else")
            response_data = {'success': True, 'message': 'Soc dins else.'}
            return JsonResponse(response_data)
        

        
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework import generics
   
# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self,request,*args,**kwargs):
        user = CustomUser.objects.get(username=request.user.username)
        serializer = UserSerializer(user)
        return Response(serializer.data)


#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_view(request):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)      
    
class UserLoginAPI(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (AllowAny,)
    def post(self,request,*args,**kwargs):
        
        #obtenir parametres
        try:
            username = request.data.get("username")
            password = request.data.get("password")
        except:
            return Response(status=HTTP_400_BAD_REQUEST)
        
        #obtenir usuari
        try:
            user = CustomUser.objects.get(username = request.user.username)
        except:
            return Response(status=HTTP_401_UNAUTHORIZED)
        
        print(user.username)
        #user = CustomUser.objects.get(username=user_auth.get_username())
        
        try:
            user_token = Token.objects.get(user=user)
        except:
            user_token = Token.objects.create(user=user)
        
        data = {'token': user_token.key}
        
        return Response(data=data, status=HTTP_200_OK)
    
    '''

from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from users.serializers import UserSerializer
from users.permissions import IsCreationOrIsAuthenticated

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsCreationOrIsAuthenticated,)
    

    

    
    


@api_view(['PUT'])
def edit_perfil(request, cif):
    try:
        perfil = Perfil.objects.get(CIF = cif)
    except Perfil.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data_cif = json.dumps(request.data.get('CIF')).strip('"').strip()
        if (len(data_cif) == 9 and not data_cif[0].isnumeric() and not data_cif[8].isnumeric() and data_cif[1:7].isnumeric()):
            serializer = PerfilSerializer(perfil, data=request.data, partial= True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                print(serializer.error_messages)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'El valor del nuevo CIF introducido es incorrecto'} , status=status.HTTP_400_BAD_REQUEST)
