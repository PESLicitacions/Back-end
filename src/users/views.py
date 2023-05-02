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

# Create your views here.
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
                response_data = {'success': True}
            else:
                response_data = {'success': False, 'message': 'Username or password incorrect'}
            return JsonResponse(response_data)

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
            print("Se ha creado el usuario con username: "+ customUs.username)
            response_data = {'success': True, 'message': 'El usuario se ha registrado correctamente.'}
            print(response_data)
            return JsonResponse(response_data)
        else: 
            print("HE entrar a l'else")
            response_data = {'success': True, 'message': 'Soc dins else.'}
            return JsonResponse(response_data)


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
