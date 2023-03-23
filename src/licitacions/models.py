from django.db import models
from licitacions import choices

# Create your models here.

class Localitzacio(models.Model):
    nom = models.CharField(max_length=100, primary_key=True)
    longitud = models.DecimalField(max_digits=22, decimal_places=16)
    latitud = models.DecimalField(max_digits=22, decimal_places=16)


class Ambit(models.Model):
    codi = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100, verbose_name="nom àmbit")


class Departament(models.Model):
    codi = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100, verbose_name="nom departament")


class Organ(models.Model):
    codi = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100, verbose_name="nom organ")


class LicitacioPublica(models.Model):
    procediment = models.CharField(max_length=150, choices=choices.procediments)
    fase_publicacio = models.CharField(max_length=80, choices=choices.fase_publicacio)
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
    enllaç = models.URLField()
    lloc_execucio = models.ForeignKey(Localitzacio, to_field='nom' , related_name="licitacio_publica", null=True, on_delete=models.SET_NULL)


class LicitacioPrivada(models.Model):
    procediment = models.CharField(max_length=150, choices=choices.procediments)
    fase_publicacio = models.CharField(max_length=80, choices=choices.fase_publicacio)
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
    lloc_execucio = models.ForeignKey(Localitzacio, related_name="licitacio_privada", null=True, on_delete=models.SET_NULL)


