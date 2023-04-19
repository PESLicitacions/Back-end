from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
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
    #print("SOC DINS EL REGISTER")
    #if request.user.is_authenticated:
    #    print("SOC DINS IF")
     #   return JsonResponse({'success': True})
    #else:
    print("HOLA")
    print(request.method)
    if request.method == 'POST':
        print("DINS EL POST")
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
    
        customUs = CustomUser.objects.create(
            email = email,
            username = username,
            password = password,
            name = name,
        )
        print("El custom user es "+ customUs.username)

        return JsonResponse({'success': True})
    else: 
        print("HE entrar a l'else")
        return JsonResponse({'success': False})

