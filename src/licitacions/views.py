from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from .models import ListaFavorits

# Create your views here.
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def unfollow_licitacio(request, id_licitacio):
    try:
        relació = ListaFavorits.objects.get(licitacio = id_licitacio, user = request.user)
    except ListaFavorits.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        relació.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def toggle_notification(request, id_licitacio):
    try:
        relacio = ListaFavorits.objects.get(licitacio = id_licitacio, user = request.user)
    except ListaFavorits.DoesNotExist:
        return Response({'error:' 'Antes de activar las notificaciones tiene que seguir a la licitacion'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
            if(relacio.notificacions == True):
                relacio.notificacions = False 
            else:
                relacio.notificacions = True 
            relacio.save()
            return Response({'Notificaciones:' 'Seguimiento por notificaciones actualizado'} , status=status.HTTP_200_OK)
