from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework import generics
from django.db.models import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView


from licitacions.models import *
from users.models import *
from licitacions.serializers import *
from users.models import CustomUser




class LicitacionsList(generics.ListAPIView):
    serializer_class = LicitacioPreviewSerializer

    def get_queryset(self):
        queryset = Licitacio.objects.all()

        localitzacio = self.request.query_params.get('lloc_execucio')
        if localitzacio is not None:
            queryset = queryset.filter(lloc_execucio__nom__icontains=localitzacio)

        pressupost_min = self.request.query_params.get('pressupost_min')
        if pressupost_min is not None:
            queryset = queryset.filter(pressupost__gte=pressupost_min)
        
        pressupost_max = self.request.query_params.get('pressupost_max')
        if pressupost_max is not None:
            queryset = queryset.filter(pressupost__lte=pressupost_max)
        
        tipus_contracte = self.request.query_params.get('tipus_contracte')
        if tipus_contracte is not None:
            queryset = queryset.filter(tipus_contracte_id=tipus_contracte)
        
        duracio_min = self.request.query_params.get('duracio_min')
        if duracio_min is not None:
            queryset = queryset.filter(duracio_contracte__gte=duracio_min)
        
        duracio_max = self.request.query_params.get('duracio_max')
        if duracio_max is not None:
            queryset = queryset.filter(duracio_contracte__lte=duracio_max)
        
        data_inici = self.request.query_params.get('data_inici')
        if data_inici is not None:
            queryset = queryset.filter(data_inici__gte=data_inici)

        data_fi = self.request.query_params.get('data_fi')
        if data_fi is not None:
            queryset = queryset.filter(data_fi__lte=data_fi)

        return queryset



class LicitacioDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = None
        pk = self.kwargs.get('pk')
        licitacio_publica = LicitacioPublica.objects.filter(pk=pk)
        if licitacio_publica.exists():
            queryset = LicitacioPublica.objects.all()
        else:
            queryset = LicitacioPrivada.objects.all()
        return queryset

    def get_serializer_class(self):
        obj = self.get_object()
        if isinstance(obj, LicitacioPublica):
            print("entered lic pub serializer")
            return LicitacioPublicaDetailsSerializer
        elif isinstance(obj, LicitacioPrivada):
            print("entered lic priv serializer")
            return LicitacioPrivadaDetailsSerializer
        else:
            return self.serializer_class

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
            #queryset = queryset.filter(ambit_id=ambit)

        departament = self.request.query_params.get('departament')
        if departament is not None:
            queryset = queryset.filter(departament__nom__icontains=departament)
            #queryset = queryset.filter(departament_id=departament)

        organ = self.request.query_params.get('organ')
        if organ is not None:
            queryset = queryset.filter(organ__nom__icontains=organ)
            #queryset = queryset.filter(organ_id=organ)
        
        tipus_contracte = self.request.query_params.get('tipus_contracte')
        if tipus_contracte is not None:
            queryset = queryset.filter(tipus_contracte_id=tipus_contracte)
        
        duracio_min = self.request.query_params.get('duracio_min')
        if duracio_min is not None:
            queryset = queryset.filter(duracio_contracte__gte=duracio_min)
        
        duracio_max = self.request.query_params.get('duracio_max')
        if duracio_max is not None:
            queryset = queryset.filter(duracio_contracte__lte=duracio_max)
        
        data_inici = self.request.query_params.get('data_inici')
        if data_inici is not None:
            queryset = queryset.filter(data_inici__gte=data_inici)

        data_fi = self.request.query_params.get('data_fi')
        if data_fi is not None:
            queryset = queryset.filter(data_fi__lte=data_fi)

        return queryset



class LicitacionsPrivadesList(generics.ListCreateAPIView):
    serializer_class = LicitacioPrivadaPreviewSerializer

    def get_queryset(self):
        queryset = LicitacioPrivada.objects.all()

        localitzacio = self.request.query_params.get('lloc_execucio')
        if localitzacio is not None:
            queryset = queryset.filter(lloc_execucio__nom__icontains=localitzacio)

        pressupost_min = self.request.query_params.get('pressupost_min')
        if pressupost_min is not None:
            queryset = queryset.filter(pressupost__gte=pressupost_min)
        
        pressupost_max = self.request.query_params.get('pressupost_max')
        if pressupost_max is not None:
            queryset = queryset.filter(pressupost__lte=pressupost_max)
        
        tipus_contracte = self.request.query_params.get('tipus_contracte')
        if tipus_contracte is not None:
            queryset = queryset.filter(tipus_contracte_id=tipus_contracte)
        
        duracio_min = self.request.query_params.get('duracio_min')
        if duracio_min is not None:
            queryset = queryset.filter(duracio_contracte__gte=duracio_min)
        
        duracio_max = self.request.query_params.get('duracio_max')
        if duracio_max is not None:
            queryset = queryset.filter(duracio_contracte__lte=duracio_max)
        
        data_inici = self.request.query_params.get('data_inici')
        if data_inici is not None:
            queryset = queryset.filter(data_inici__gte=data_inici)

        data_fi = self.request.query_params.get('data_fi')
        if data_fi is not None:
            queryset = queryset.filter(data_fi__lte=data_fi)

        return queryset
   
    

class LicitacionsFavoritesList(generics.ListAPIView):
    authentication_classes(IsAuthenticated,)
    permission_classes(TokenAuthentication,)
    serializer_class = LicitacioPreviewSerializer

    def get_queryset(self):
        user = self.request.user
        favorits = ListaFavorits.objects.filter(user=user).values_list('licitacio_id', flat=True)
        return Licitacio.objects.filter(id__in=favorits)
    
class LicitacionsSeguidesList(generics.ListAPIView):
    authentication_classes(IsAuthenticated,)
    permission_classes(TokenAuthentication,)
    serializer_class = LicitacioPreviewSerializer

    def get_queryset(self):
        user = self.request.user
        seguint = ListaFavorits.objects.filter(user=user, notificacions = True).values_list('licitacio_id', flat=True)
        return Licitacio.objects.filter(id__in=seguint)

class LicitacionsFollowingList(generics.ListAPIView):
    authentication_classes(IsAuthenticated,)
    permission_classes(TokenAuthentication,)
    serializer_class = LicitacioPrivadaPreviewSerializer

    def get_queryset(self):
        user = self.request.user
        favorits = ListaFavorits.objects.filter(user=user, notificacions = True).values_list('licitacio_id', flat=True)
        return Licitacio.objects.filter(id__in=favorits)


class LocalitzacionsInfo(generics.ListAPIView):
    serializer_class = LocalitzacioInfoSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = Localitzacio.objects.all().order_by('nom')

        localitzacio = self.request.query_params.get('lloc_execucio')
        if localitzacio is not None:
            queryset = queryset.filter(nom__icontains=localitzacio)
        return queryset


class AmbitsInfo(generics.ListAPIView):
    serializer_class = AmbitInfoSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = Ambit.objects.all().order_by('nom')

        ambit = self.request.query_params.get('ambit')
        if ambit is not None:
            queryset = queryset.filter(nom__icontains=ambit)
        return queryset


class DepartamentsInfo(generics.ListAPIView):
    serializer_class = DepartamentInfoSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = Departament.objects.all().order_by('nom')

        departament = self.request.query_params.get('departament')
        if departament is not None:
            queryset = queryset.filter(nom__icontains=departament)
        return queryset
    

class OrgansInfo(generics.ListAPIView):
    serializer_class = OrganInfoSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = Organ.objects.all().order_by('nom')

        organ = self.request.query_params.get('organ')
        if organ is not None:
            queryset = queryset.filter(nom__icontains=organ)
        return queryset


class TipusContracteInfo(generics.ListAPIView):
    serializer_class = TipusContracteInfoSerializer
    pagination_class = None
    
    def get_queryset(self):
        queryset = TipusContracte.objects.all().order_by('tipus_contracte')

        tipus_contracte = self.request.query_params.get('tipus_contracte')
        if tipus_contracte is not None:
            queryset = queryset.filter(Q(tipus_contracte__icontains=tipus_contracte) | Q(subtipus_contracte__icontains=tipus_contracte))
        return queryset

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = None
        cif = self.kwargs.get('cif')
        user = Perfil.objects.get(CIF = cif)
        if user.exists():
            queryset = LicitacioPublica.objects.all()
        else:
            queryset = LicitacioPrivada.objects.all()
        return queryset

class Add_to_favorites(APIView):
    authentication_classes(IsAuthenticated,)
    permission_classes(TokenAuthentication,)
    
    def post(self,request, pk):
        user = request.user
        licitacio = get_object_or_404(Licitacio, pk=pk)
        favorit = ListaFavorits.objects.filter(user=user, licitacio=licitacio).first()
        if favorit:
            favorit.delete()
            response_data = {'licitacio': pk, 'user': user.email, 'action': 'deleted from favorites', 'success': True}
        else:
            favorit = ListaFavorits(user=user, licitacio=licitacio)
            favorit.save()
            response_data = {'licitacio': pk, 'user': user.email, 'action': 'added to favorites', 'success': True}
        return JsonResponse(response_data)

class Add_to_seguint(APIView):
    authentication_classes(IsAuthenticated,)
    permission_classes(TokenAuthentication,)
    
    def post(self,request, pk):
        user = request.user
        licitacio = get_object_or_404(Licitacio, pk=pk)
        seguir = ListaFavorits.objects.filter(user=user, licitacio=licitacio).first()
        if seguir:
            if seguir.notificacions == True:
                seguir.notificacions=False
                seguir.save()
                response_data = {'licitacio': pk, 'user': user.email, 'action': 'deleted from seguint', 'success': True}
            else:
                seguir.notificacions=True
                seguir.save() 
                response_data = {'licitacio': pk, 'user': user.email, 'action': 'added to seguint', 'success': True}
        else:
            response_data = {'licitacio': pk, 'user': user.email, 'action': 'First add it to favorites', 'success': False}
        
        return JsonResponse(response_data)

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def add_to_preferences(request, pk):
    user = request.user
    tipus_contracte = get_object_or_404(TipusContracte, pk=pk)

    preference = Preference.objects.filter(user=user, tipus_contracte=tipus_contracte).first()
    if preference:
        preference.delete()
        response_data = {'tipus_contracte': pk, 'user': user.id, 'action': 'deleted from preferences', 'success': True}
    else:
        preference = Preference(user=user, tipus_contracte=tipus_contracte)
        preference.save()
        response_data = {'tipus_contracte': pk, 'user': user.id, 'action': 'added to preferences', 'success': True}
    return JsonResponse(response_data)