from django.http import HttpResponse
from licitacions import models, serializers
from rest_framework import viewsets, permissions


class LicitacioPublicaViewSet(viewsets.ModelViewSet):
    queryset = models.LicitacioPublica.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.LicitacioPublicaSerializer


class LicitacioPrivadaViewSet(viewsets.ModelViewSet):
    queryset = models.LicitacioPrivada.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.LicitacioPrivadaSerializer


class TipusContracteViewSet(viewsets.ModelViewSet):
    queryset = models.TipusContracte.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.TipusContracteSerializer


class LocalitzacioViewSet(viewsets.ModelViewSet):
    queryset = models.Localitzacio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.LocalitzacioSerializer


class AmbitViewSet(viewsets.ModelViewSet):
    queryset = models.Ambit.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.AmbitSerializer


class DepartamentViewSet(viewsets.ModelViewSet):
    queryset = models.Departament.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.DepartamentSerializer


class OrganViewSet(viewsets.ModelViewSet):
    queryset = models.Organ.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.OrganSerializer

class BarcelonaViewSet(viewsets.ModelViewSet):
    queryset = models.Localitzacio.objects.filter(nom='Barcelona')
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.LocalitzacioSerializer
