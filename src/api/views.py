from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from licitacions.models import *
from licitacions.serializers import *

@api_view(["GET"])
def licitacions_publiques_preview(request):
    instance = LicitacioPublica.objects.all().first()
    data = {}
    if instance:
        data = LicitacioPublicaPreviewSerializer(instance).data
        print(data)
    return Response(data)


@api_view(["GET"])
def licitacio_publica_detail(request):
    instance = LicitacioPublica.objects.all().first()
    data = {}
    if instance:
        data = LicitacioPublicaDetailsSerializer(instance).data
        print(data)
    return Response(data)


@api_view(["GET"])
def licitacions_privades_preview(request):
    instance = LicitacioPrivada.objects.all()
    data = {}
    if instance:
        data = LicitacioPrivadaPreviewSerializer(instance).data
        print(data)
    return Response(data)


@api_view(["GET"])
def licitacio_privada_detail(request):
    instance = LicitacioPrivada.objects.all().first()
    data = {}
    if instance:
        data = LicitacioPrivadaDetailsSerializer(instance).data
        print(data)
    return Response(data)
