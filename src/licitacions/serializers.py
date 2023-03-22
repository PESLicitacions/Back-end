from rest_framework import serializers
from .models import Licitacio

class LicitacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licitacio
        fields = ('id', 'fase_publicacio', 'denominacio', 'objecte_contracte', 'pressupost', 'valor_estimat_contracte',
                  'valor_estimat_contracte', 'duracio_contracte', 'termini_presentacio_ofertes', 'data_publicacio_anunci',
                  'data_publicacio_adjudicacio', 'codi_cpv', 'import_adjudicacio_sense_iva', 'import_adjudicacio_amb_iva',
                  'ofertes_rebudes', 'resultat', 'data_adjudicacio_contracte', 'data_formalitzacio_contracte')