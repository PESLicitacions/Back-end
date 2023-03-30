from rest_framework import serializers
from licitacions import models

class LicitacioPublicaPreviewSerializer(serializers.ModelSerializer):
    tipus_contracte = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.LicitacioPublica
        fields = ('id', 'lloc_execucio', 'pressupost', 'denominacio', 'tipus_contracte')


class LicitacioPublicaDetailsSerializer(serializers.ModelSerializer):
    tipus_contracte = serializers.StringRelatedField(many=False)
    ambit = serializers.StringRelatedField(many=False)
    departament = serializers.StringRelatedField(many=False)
    organ = serializers.StringRelatedField(many=False)
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
