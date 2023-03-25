from django.shortcuts import render
from django.db import transaction
from django.http import JsonResponse
from licitacions.models import Localitzacio, Ambit, Departament, Organ, TipusContracte, LicitacioPublica, LicitacioPrivada
import requests
import json


def get_data(request):
    PARAMS = 'procediment, fase_publicacio, denominacio, objecte_contracte, pressupost_licitacio, valor_estimat_contracte, duracio_contracte, termini_presentacio_ofertes, data_publicacio_anunci, data_publicacio_adjudicacio, codi_cpv, import_adjudicacio_sense, import_adjudicacio_amb_iva, ofertes_rebudes, resultat, data_adjudicacio_contracte, data_formalitzacio_contracte, enllac_publicacio, lloc_execucio'
    num_rows = '10'
    base_url = 'https://analisi.transparenciacatalunya.cat/resource/a23c-d6vp.json?$query=SELECT ' + PARAMS + ' LIMIT ' + num_rows
    response_API = requests.get(base_url)
    data = response_API.text
    parse_json = json.loads(data)
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
            if(data_publicacio_anunci != None):
                resultsplit = data_publicacio_anunci.split('T')
                data_publicacio_anunci = str(resultsplit[0])

            data_publicacio_adjudicacio = licitacio.get('data_publicacio_adjudicacio')
            if(data_publicacio_adjudicacio != None):           
                resultsplit = data_publicacio_adjudicacio.split('T')
                data_publicacio_adjudicacio = str(resultsplit[0])

            codi_cpv = licitacio.get('codi_cpv')
            import_adjudicacio_sense_iva = licitacio.get('import_adjudicacio_sense')
            import_adjudicacio_amb_iva = licitacio.get('import_adjudicacio_amb_iva')
            ofertes_rebudes = licitacio.get('ofertes_rebudes')
            resultat = licitacio.get('resultat')

            data_adjudicacio_contracte = licitacio.get('data_adjudicacio_contracte')
            if(data_adjudicacio_contracte != None):
                resultsplit = data_adjudicacio_contracte.split('T')
                data_adjudicacio_contracte = str(resultsplit[0])

            
            data_formalitzacio_contracte = licitacio.get('data_formalitzacio_contracte')
            if(data_formalitzacio_contracte != None):
                resultsplit = data_formalitzacio_contracte.split('T')
                data_formalitzacio_contracte = str(resultsplit[0])

            enllaç = licitacio.get('enllac_publicacio')
            lloc_execucio = None
            ambit = None
            departament = None
            organ = None
            tipus_contracte = None
            l = LicitacioPublica.objects.create(procediment = procediment,
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
            
    return JsonResponse(data, safe=False)

 
