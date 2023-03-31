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


class LocalitzacioInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Localitzacio
        fields = ('nom',)


class AmbitInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ambit
        fields = '__all__'


class DepartamentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departament
        fields = '__all__'


class OrganInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organ
        fields = '__all__'


class TipusContracteInfoSerializer(serializers.ModelSerializer):
    contracte_str = serializers.SerializerMethodField()
    class Meta:
        model = models.TipusContracte
        fields = ('id', 'contracte_str')
    
    def get_contracte_str(self, obj):
        return str(obj)
