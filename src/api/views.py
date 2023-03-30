from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from django.db.models import Q

from licitacions.models import *
from licitacions.serializers import *


class LicitacionsPubliquesList(generics.ListAPIView):
    serializer_class = LicitacioPublicaPreviewSerializer
    
    def get_queryset(self):
        queryset = LicitacioPublica.objects.all()

        localitzacio = self.request.query_params.get('lloc_execucio')
        if localitzacio is not None:
            queryset = queryset.filter(lloc_execucio__nom__icontains=localitzacio)

        pressupost_min = self.request.query_params.get('pressupost_min')
        if pressupost_min is not None:
            queryset = queryset.filter(pressupost__gte=pressupost_min)
        
        pressupost_max = self.request.query_params.get('pressupost_max')
        if pressupost_max is not None:
            queryset = queryset.filter(pressupost__lte=pressupost_max)
        
        ambit = self.request.query_params.get('ambit')
        if ambit is not None:
            queryset = queryset.filter(ambit__nom__icontains=ambit)

        departament = self.request.query_params.get('departament')
        if departament is not None:
            queryset = queryset.filter(departament__nom__icontains=departament)

        organ = self.request.query_params.get('organ')
        if organ is not None:
            queryset = queryset.filter(organ__nom__icontains=organ)
        
        tipus_contracte = self.request.query_params.get('tipus_contracte')
        if tipus_contracte is not None:
            queryset = queryset.filter(Q(tipus_contracte__tipus_contracte__icontains=tipus_contracte) | Q(tipus_contracte__subtipus_contracte__icontains=tipus_contracte))

        return queryset
    
        
class LicitacioPublicaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LicitacioPublica.objects.all()
    serializer_class = LicitacioPublicaDetailsSerializer

class LicitacionsPrivadesList(generics.ListCreateAPIView):
    queryset = LicitacioPrivada.objects.all()
    serializer_class = LicitacioPrivadaPreviewSerializer

class LicitacioPrivadaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LicitacioPrivada.objects.all()
    serializer_class = LicitacioPrivadaDetailsSerializer

