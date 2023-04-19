from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json

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
