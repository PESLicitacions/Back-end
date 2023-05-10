from rest_framework import serializers
from licitacions import models
from .models import ListaFavorits

class LicitacioPreviewSerializer(serializers.ModelSerializer):
    tipus_contracte = serializers.StringRelatedField(many=False)
    favorit = serializers.SerializerMethodField()
    notificacions = serializers.SerializerMethodField()

    class Meta:
        model = models.Licitacio
        fields = ('id', 'lloc_execucio', 'pressupost', 'denominacio', 'tipus_contracte', 'favorit', 'notificacions')
    
    def get_favorit(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            try:
                models.ListaFavorits.objects.get(user=user, licitacio=obj)
                return True
            except models.ListaFavorits.DoesNotExist:
                pass
        return False
    
    def get_notificacions(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            try:
                models.ListaFavorits.objects.get(user=user, licitacio=obj, notificacions = True)
                return True
            except models.ListaFavorits.DoesNotExist:
                pass
        return False

class LicitacioPublicaPreviewSerializer(serializers.ModelSerializer):
    tipus_contracte = serializers.StringRelatedField(many=False)
    favorit = serializers.SerializerMethodField()


    class Meta:
        model = models.LicitacioPublica
        fields = ('id', 'lloc_execucio', 'pressupost', 'denominacio', 'tipus_contracte', 'favorit')
    
    def get_favorit(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            try:
                models.ListaFavorits.objects.get(user=user, licitacio=obj)
                return True
            except models.ListaFavorits.DoesNotExist:
                pass
        return False



class LicitacioPublicaDetailsSerializer(serializers.ModelSerializer):
    tipus_contracte = serializers.StringRelatedField(many=False)
    ambit = serializers.StringRelatedField(many=False)
    departament = serializers.StringRelatedField(many=False)
    organ = serializers.StringRelatedField(many=False)
    favorit = serializers.SerializerMethodField()

    class Meta:
        model = models.LicitacioPublica
        fields = '__all__'
    
    def get_favorit(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            try:
                models.ListaFavorits.objects.get(user=user, licitacio=obj)
                return True
            except models.ListaFavorits.DoesNotExist:
                pass
        return False
    


class LicitacioPrivadaPreviewSerializer(serializers.ModelSerializer):
    favorit = serializers.SerializerMethodField()

    class Meta:
        model = models.LicitacioPrivada
        fields = ('id', 'lloc_execucio', 'pressupost', 'denominacio', 'tipus_contracte', 'favorit')
    
    def get_favorit(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            try:
                models.ListaFavorits.objects.get(user=user, licitacio=obj)
                return True
            except models.ListaFavorits.DoesNotExist:
                pass
        return False
    



class LicitacioPrivadaDetailsSerializer(serializers.ModelSerializer):
    favorit = serializers.SerializerMethodField()

    class Meta:
        model = models.LicitacioPrivada
        fields = '__all__'
    
    def get_favorit(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            try:
                models.ListaFavorits.objects.get(user=user, licitacio=obj)
                return True
            except models.ListaFavorits.DoesNotExist:
                pass
        return False
    


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


class ListaFavoritsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaFavorits
        fields = '__all__'
