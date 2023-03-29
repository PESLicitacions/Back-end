from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView

from licitacions.models import *
from licitacions.serializers import *


class licitacions_publiques(APIView):
    def get(self, request):
        licitacions_publiques = LicitacioPublica.objects.all()
        serializer = LicitacioPublicaPreviewSerializer(licitacions_publiques, many=True)
        print(serializer.data)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = LicitacioPublicaDetailsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            print(instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class licitacio_publica_detail(APIView):
    def get_object(self, pk):
        try:
            return LicitacioPublica.objects.get(pk=pk)
        except LicitacioPublica.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        lpub = self.get_object(pk)
        serializer = LicitacioPublicaDetailsSerializer(lpub)
        return Response(serializer.data)


    def put(self, request, pk):
        lpub = self.get_object(pk)
        serializer = LicitacioPublicaDetailsSerializer(lpub, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        lpub = self.get_object(pk)
        lpub.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class licitacions_privades(APIView):
    def get(self, request):
        licitacions_privades = LicitacioPrivada.objects.all()
        serializer = LicitacioPrivadaPreviewSerializer(licitacions_privades, many=True)
        print(serializer.data)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = LicitacioPrivadaDetailsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            print(instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class licitacio_privada_detail(APIView):
    def get_object(self, pk):
        try:
            return LicitacioPrivada.objects.get(pk=pk)
        except LicitacioPrivada.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        lpriv = self.get_object(pk)
        serializer = LicitacioPrivadaDetailsSerializer(lpriv)
        return Response(serializer.data)


    def put(self, request, pk):
        lpriv = self.get_object(pk)
        serializer = LicitacioPrivadaDetailsSerializer(lpriv, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        lpriv = self.get_object(pk)
        lpriv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
