from django.shortcuts import render
from django.db import transaction
from django.http import JsonResponse
from licitacions.models import Licitacio
import requests
import json


def get_data(request):
    PARAMS = 'procediment, fase_publicacio, denominacio, objecte_contracte, pressupost_licitacio, valor_estimat_contracte, duracio_contracte, termini_presentacio_ofertes, data_publicacio_anunci, data_publicacio_adjudicacio, codi_cpv, import_adjudicacio_sense, import_adjudicacio_amb_iva, ofertes_rebudes, resultat, data_adjudicacio_contracte, data_formalitzacio_contracte'
    num_rows = '10'
    base_url = 'https://analisi.transparenciacatalunya.cat/resource/a23c-d6vp.json?$query=SELECT ' + PARAMS + ' LIMIT ' + num_rows
    response_API = requests.get(base_url)
    data = response_API.text
    #print('DATA RESPONSE:')
    #print(data)
    parse_json = json.loads(data)
    #print('JSON DATA')
    # print(parse_json)
    with transaction.atomic():
        for licitacio in parse_json:
            procediment = licitacio.get('procediment')
            fase_publicacio = licitacio.get('fase_publicacio')
            denominacio = licitacio.get('denominacio')
            objecte_contracte = licitacio.get('objecte_contracte')
            pressupost_licitacio = licitacio.get('pressupost_licitacio')
            valor_estimat_contracte = licitacio.get('valor_estimat_contracte')
            duracio_contracte = licitacio.get('duracio_contracte')
            termini_presentacio_ofertes = licitacio.get('termini_presentacio_ofertes')
            data_publicacio_anunci = licitacio.get('data_publicacio_anunci')
            data_publicacio_adjudicacio = licitacio.get('data_publicacio_adjudicacio')
            codi_cpv = licitacio.get('codi_cpv')
            import_adjudicacio_sense_iva = licitacio.get('import_adjudicacio_sense')
            import_adjudicacio_amb_iva = licitacio.get('import_adjudicacio_amb_iva')
            ofertes_rebudes = licitacio.get('ofertes_rebudes')
            resultat = licitacio.get('resultat')
            data_adjudicacio_contracte = licitacio.get('data_adjudicacio_contracte')
            data_formalitzacio_contracte = licitacio.get('data_formalitzacio_contracte')
            l = Licitacio.objects.create(procediment = procediment,
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
                            data_formalitzacio_contracte = data_formalitzacio_contracte
                            )
            #l.save()
            
    return JsonResponse(data, safe=False)


def import_data_to_DB(request):
   return 'yes'
   '''
     json = get_data(request)
    with transaction.atomic():
        for licitacio in json:
            Licitacio.objects.create(**json)
'''