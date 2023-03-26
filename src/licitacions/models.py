from django.db import models
from licitacions import choices

# Create your models here.

class Localitzacio(models.Model):
    nom = models.CharField(max_length=100, primary_key=True)
    longitud = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    latitud = models.DecimalField(max_digits=22, decimal_places=16, null=True)

    def __str__(self):
        return self.nom


class Ambit(models.Model):
    codi = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100, verbose_name="nom àmbit")

    def __str__(self):
        return self.nom


class Departament(models.Model):
    codi = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100, verbose_name="nom departament")

    def __str__(self):
        return self.nom


class Organ(models.Model):
    codi = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100, verbose_name="nom organ")

    def __str__(self):
        return self.nom


class TipusContracte(models.Model):
    tipus_contracte = models.CharField(max_length=50)
    subtipus_contracte = models.CharField(max_length=250)

    class Meta:
        unique_together = ('tipus_contracte', 'subtipus_contracte')

    def __str__(self):
        return self.tipus_contracte + ': ' + self.subtipus_contracte


class LicitacioPublica(models.Model):
    id = models.BigAutoField(primary_key=True)
    procediment = models.CharField(max_length=150, choices=choices.procediments, null=True)
    fase_publicacio = models.CharField(max_length=80, choices=choices.fase_publicacio, null=True)
    denominacio = models.TextField(null=True)
    objecte_contracte = models.TextField(null=True)
    pressupost = models.DecimalField(decimal_places=2, max_digits=100, null=True)
    valor_estimat_contracte = models.DecimalField(decimal_places=2, max_digits=100, null=True)
    duracio_contracte = models.CharField(max_length=80, null=True)
    termini_presentacio_ofertes = models.DateTimeField(null=True)
    data_publicacio_anunci = models.DateTimeField(null=True)
    data_publicacio_adjudicacio = models.DateTimeField(null=True)
    codi_cpv = models.IntegerField(null=True)
    import_adjudicacio_sense_iva = models.DecimalField(decimal_places=2, max_digits=100, null=True)
    import_adjudicacio_amb_iva = models.DecimalField(decimal_places=2, max_digits=100, null=True)
    ofertes_rebudes = models.IntegerField(null=True)
    resultat = models.CharField(max_length=50, null=True)
    data_adjudicacio_contracte = models.DateField(null=True)
    data_formalitzacio_contracte = models.DateField(null=True)
    enllaç = models.URLField(null=True)
    lloc_execucio = models.ForeignKey(Localitzacio, to_field='nom', related_name="licitacio_publica", null=True, on_delete=models.SET_NULL)
    ambit = models.ForeignKey(Ambit, to_field='codi', related_name="licitacio_publica", null=True, on_delete=models.SET_NULL)
    departament = models.ForeignKey(Departament, to_field='codi', related_name="licitacio_publica", null=True, on_delete=models.SET_NULL)
    organ = models.ForeignKey(Organ, to_field='codi', related_name="licitacio_publica", null=True, on_delete=models.SET_NULL)
    tipus_contracte = models.ForeignKey(TipusContracte, to_field='id', related_name="licitacio_publica", null=True, on_delete=models.SET_NULL)

class LicitacioPrivada(models.Model):
    procediment = models.CharField(max_length=150, choices=choices.procediments, null=True)
    fase_publicacio = models.CharField(max_length=80, choices=choices.fase_publicacio, null=True)
    denominacio = models.TextField(null=True)
    objecte_contracte = models.TextField(null=True)
    pressupost = models.DecimalField(decimal_places=2, max_digits=9, null=True)
    valor_estimat_contracte = models.DecimalField(decimal_places=2, max_digits=9, null=True)
    duracio_contracte = models.CharField(max_length=80, null=True)
    termini_presentacio_ofertes = models.DateTimeField(null=True)
    data_publicacio_anunci = models.DateTimeField(null=True)
    data_publicacio_adjudicacio = models.DateTimeField(null=True)
    codi_cpv = models.IntegerField(null=True)
    import_adjudicacio_sense_iva = models.DecimalField(decimal_places=2, max_digits=9, null=True)
    import_adjudicacio_amb_iva = models.DecimalField(decimal_places=2, max_digits=9, null=True)
    ofertes_rebudes = models.IntegerField(null=True)
    resultat = models.CharField(max_length=50, null=True)
    data_adjudicacio_contracte = models.DateField(null=True)
    data_formalitzacio_contracte = models.DateField(null=True)
    lloc_execucio = models.ForeignKey(Localitzacio, related_name="licitacio_privada", null=True, on_delete=models.SET_NULL)
    tipus_contracte = models.ForeignKey(TipusContracte, to_field='id', related_name="licitacio_privada", null=True, on_delete=models.SET_NULL)


