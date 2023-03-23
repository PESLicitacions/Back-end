from rest_framework import serializers
from licitacions import models

class LicitacioPublicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LicitacioPublica
        fields = '__all__'


class LicitacioPrivadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LicitacioPrivada
        fields = '__all__'


class LocalitzacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Localitzacio
        fields = '__all__'


class AmbitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ambit
        fields = '__all__'


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departament
        fields = '__all__'


class OrganSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organ
        fields = '__all__'