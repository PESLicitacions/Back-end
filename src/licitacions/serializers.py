from rest_framework import serializers
from licitacions import models

class LicitacioPublicaPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LicitacioPublica
        fields = ('id', 'lloc_execucio', 'pressupost', 'denominacio', 'tipus_contracte')


class LicitacioPublicaDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LicitacioPublica
        fields = '__all__'


class LicitacioPrivadaPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LicitacioPrivada
        fields = ('id', 'lloc_execucio', 'pressupost', 'denominacio', 'tipus_contracte')


class LicitacioPrivadaDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LicitacioPrivada
        fields = '__all__'
