from django.db import models

# Create your models here.
class Licitacio(models.Model):
    procediment = models.CharField(max_length=50)
    fase_publicacio = models.CharField(max_length=80)
    denominacio = models.TextField()
    objecte_contracte = models.TextField()
    pressupost = models.DecimalField(decimal_places=2, max_digits=9)
    valor_estimat_contracte = models.DecimalField(decimal_places=2, max_digits=9)
    duracio_contracte = models.CharField(max_length=80)
    termini_presentacio_ofertes = models.DateTimeField()
    data_publicacio_anunci = models.DateTimeField()
    data_publicacio_adjudicacio = models.DateTimeField()
    codi_cpv = models.IntegerField()
    import_adjudicacio_sense_iva = models.DecimalField(decimal_places=2, max_digits=9)
    import_adjudicacio_amb_iva = models.DecimalField(decimal_places=2, max_digits=9)
    ofertes_rebudes = models.IntegerField()
    resultat = models.CharField(max_length=50)
    data_adjudicacio_contracte = models.DateField()
    data_formalitzacio_contracte = models.DateField()


