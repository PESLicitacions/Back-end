from django.shortcuts import render
from django.db import transaction
from django.http import JsonResponse
from licitacions.models import Localitzacio, Ambit, Departament, Organ, TipusContracte, LicitacioPublica, LicitacioPrivada
from decimal import Decimal, getcontext
import requests
import json


def get_data(request):
    PARAMS = 'procediment, fase_publicacio, denominacio, objecte_contracte, pressupost_licitacio, valor_estimat_contracte, duracio_contracte, termini_presentacio_ofertes, data_publicacio_anunci, data_publicacio_adjudicacio, codi_cpv, import_adjudicacio_sense, import_adjudicacio_amb_iva, ofertes_rebudes, resultat, data_adjudicacio_contracte, data_formalitzacio_contracte, enllac_publicacio, lloc_execucio, codi_ambit, nom_ambit, codi_departament_ens, nom_departament_ens'
    num_rows = '20'
    base_url = 'https://analisi.transparenciacatalunya.cat/resource/a23c-d6vp.json?$query=SELECT ' + PARAMS + ' LIMIT ' + num_rows
    response_API = requests.get(base_url)
    data = response_API.text
    print(data)
    parse_json = json.loads(data)


    with transaction.atomic():
        for licitacio in parse_json:
            procediment = licitacio.get('procediment')
            fase_publicacio = licitacio.get('fase_publicacio')
            denominacio = licitacio.get('denominacio')
            objecte_contracte = licitacio.get('objecte_contracte')

            pressupost_licitacio = licitacio.get('pressupost_licitacio')
            if(pressupost_licitacio is None):
                pressupost_licitacio = 0.00
            else: 
                pressupost_licitacio = Decimal(pressupost_licitacio)

            valor_estimat_contracte = licitacio.get('valor_estimat_contracte')
            if(valor_estimat_contracte is None):
                valor_estimat_contracte = 0.00
            else: 
                valor_estimat_contracte = Decimal(valor_estimat_contracte)

                
            duracio_contracte = licitacio.get('duracio_contracte')

            termini_presentacio_ofertes = licitacio.get('termini_presentacio_ofertes')
            if(termini_presentacio_ofertes is not None):
                resultsplit = termini_presentacio_ofertes.split('T')
                termini_presentacio_ofertes = str(resultsplit[0])

            data_publicacio_anunci = licitacio.get('data_publicacio_anunci')
            if(data_publicacio_anunci is not None):
                resultsplit = data_publicacio_anunci.split('T')
                data_publicacio_anunci = str(resultsplit[0])

            data_publicacio_adjudicacio = licitacio.get('data_publicacio_adjudicacio')
            if(data_publicacio_adjudicacio is not None):           
                resultsplit = data_publicacio_adjudicacio.split('T')
                data_publicacio_adjudicacio = str(resultsplit[0])

            codi_cpv = licitacio.get('codi_cpv')
            if(codi_cpv is not None):
                codi_cpv = int(codi_cpv)

            import_adjudicacio_sense_iva = licitacio.get('import_adjudicacio_sense')
            if(import_adjudicacio_sense_iva is None):
                import_adjudicacio_sense_iva = 0.00
            else:
                import_adjudicacio_sense_iva = Decimal(import_adjudicacio_sense_iva)

            
            import_adjudicacio_amb_iva = licitacio.get('import_adjudicacio_amb_iva')
            if(import_adjudicacio_amb_iva is None):
                import_adjudicacio_amb_iva = 0.00
            else:
                import_adjudicacio_amb_iva = Decimal(import_adjudicacio_amb_iva)

            

            ofertes_rebudes = licitacio.get('ofertes_rebudes')
            if(ofertes_rebudes is not None):
                ofertes_rebudes = int(ofertes_rebudes)

            resultat = licitacio.get('resultat')

            data_adjudicacio_contracte = licitacio.get('data_adjudicacio_contracte')
            if(data_adjudicacio_contracte is not None):
                resultsplit = data_adjudicacio_contracte.split('T')
                data_adjudicacio_contracte = str(resultsplit[0])

            
            data_formalitzacio_contracte = licitacio.get('data_formalitzacio_contracte')
            if(data_formalitzacio_contracte is not None):
                resultsplit = data_formalitzacio_contracte.split('T')
                data_formalitzacio_contracte = str(resultsplit[0])

            enllaç = licitacio.get('enllac_publicacio')

            lloc_execucio = get_lloc_execucio(licitacio.get('lloc_execucio'))

            ambit = get_ambit(licitacio.get('nom_ambit'), licitacio.get('codi_ambit'))

            departament = get_departament(licitacio.get('nom_departament_ens'), licitacio.get('codi_departament_ens'))
    
            organ = None
            tipus_contracte = None
            object, exists = LicitacioPublica.objects.get_or_create(procediment = procediment,
                            fase_publicacio = fase_publicacio,
                            denominacio = denominacio,
                            objecte_contracte = objecte_contracte,
                            pressupost = pressupost_licitacio,
                            valor_estimat_contracte = valor_estimat_contracte,
                            duracio_contracte = duracio_contracte,
                            termini_presentacio_ofertes = termini_presentacio_ofertes,
                            data_publicacio_anunci = data_publicacio_anunci,
                            data_publicacio_adjudicacio = data_publicacio_adjudicacio,
                            codi_cpv = codi_cpv,
                            import_adjudicacio_sense_iva = import_adjudicacio_sense_iva,
                            import_adjudicacio_amb_iva = import_adjudicacio_amb_iva,
                            ofertes_rebudes = ofertes_rebudes,
                            resultat = resultat,
                            data_adjudicacio_contracte = data_adjudicacio_contracte,
                            data_formalitzacio_contracte = data_formalitzacio_contracte,
                            enllaç = enllaç,
                            lloc_execucio = lloc_execucio,
                            ambit = ambit, 
                            departament = departament, 
                            organ = organ,
                            tipus_contracte = tipus_contracte
                            )
            
            if(exists):
                print('ya existe')

    return JsonResponse(data, safe=False)

def delete_all_licitacions_publicas(request):
    LicitacioPublica.objects.all().delete()
    return render(request, 'ok.html')


def get_lloc_execucio(lloc_execucio):
    try:
        obj = Localitzacio.objects.get(nom=lloc_execucio)
        return obj
    except Localitzacio.DoesNotExist:
        obj = Localitzacio(nom=lloc_execucio, longitud=Decimal(0.19), latitud=Decimal(0.1))
        obj.save()
        return obj

def get_ambit(nom, codi):
    try:
        obj = Ambit.objects.get(codi = codi, nom = nom)
        return obj
    except Ambit.DoesNotExist:
        obj = Ambit(codi = codi, nom = nom)
        obj.save()
        return obj
    
def get_departament(nom, codi):
    try:
        obj = Departament.objects.get(codi = codi, nom = nom)
        return obj
    except Departament.DoesNotExist:
        obj = Departament(codi = codi, nom = nom)
        obj.save()
        return obj
    