# Generated by Django 4.1.7 on 2023-03-25 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambit',
            fields=[
                ('codi', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100, verbose_name='nom àmbit')),
            ],
        ),
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('codi', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100, verbose_name='nom departament')),
            ],
        ),
        migrations.CreateModel(
            name='Localitzacio',
            fields=[
                ('nom', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('longitud', models.DecimalField(decimal_places=16, max_digits=22, null=True)),
                ('latitud', models.DecimalField(decimal_places=16, max_digits=22, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('codi', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100, verbose_name='nom organ')),
            ],
        ),
        migrations.CreateModel(
            name='TipusContracte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipus_contracte', models.CharField(max_length=50)),
                ('subtipus_contracte', models.CharField(max_length=250)),
            ],
            options={
                'unique_together': {('tipus_contracte', 'subtipus_contracte')},
            },
        ),
        migrations.CreateModel(
            name='LicitacioPublica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procediment', models.CharField(choices=[('Obert', 'Obert'), ('Contracte menor', 'Contracte menor'), ('Negociat sense publicitat', 'Negociat sense publicitat'), ('Contracte basat en acord marc', 'Contracte basat en acord marc'), ('Altres procediments segons instruccions internes', 'Altres procediments segons instruccions internes'), ('Restringit', 'Restringit'), ('Específic de Sistema Dinàmic de Adquisició', 'Específic de Sistema Dinàmic de Adquisició'), ('Concurs de projectes', 'Concurs de projectes'), ('Contracte derivat de acord marc', 'Contracte derivat de acord marc'), ('Licitació amb negociació', 'Licitació amb negociació'), ('Negociat amb publicitat', 'Negociat amb publicitat')], max_length=150, null=True)),
                ('fase_publicacio', models.CharField(choices=[('Formalització', 'Formalització'), ('Adjudicació', 'Adjudicació'), ('Anunci de licitació en avaluació', 'Anunci de licitació en avaluació'), ('Adjudicació deserta', 'Adjudicació deserta'), ('Desistiment', 'Desistiment'), ('Anul·lació de expedient', 'Anul·lació de expedient'), ('Anunci de licitació en termini', 'Anunci de licitació en termini'), ('Encàrrec a mitjà pròpi', 'Encàrrec a mitjà pròpi'), ('Decisió de no adjudicar un contracte', 'Decisió de no adjudicar un contracte'), ('Alerta de futura licitació', 'Alerta de futura licitació'), ('Anunci previ', 'Anunci previ'), ('Decisió de no subscriure un contracte', 'Decisió de no subscriure un contracte')], max_length=80, null=True)),
                ('denominacio', models.TextField(null=True)),
                ('objecte_contracte', models.TextField(null=True)),
                ('pressupost', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('valor_estimat_contracte', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('duracio_contracte', models.CharField(max_length=80, null=True)),
                ('termini_presentacio_ofertes', models.DateTimeField(null=True)),
                ('data_publicacio_anunci', models.DateTimeField(null=True)),
                ('data_publicacio_adjudicacio', models.DateTimeField(null=True)),
                ('codi_cpv', models.IntegerField(null=True)),
                ('import_adjudicacio_sense_iva', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('import_adjudicacio_amb_iva', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('ofertes_rebudes', models.IntegerField(null=True)),
                ('resultat', models.CharField(max_length=50, null=True)),
                ('data_adjudicacio_contracte', models.DateField(null=True)),
                ('data_formalitzacio_contracte', models.DateField(null=True)),
                ('enllaç', models.URLField(null=True)),
                ('ambit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='licitacio_publica', to='licitacions.ambit')),
                ('departament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='licitacio_publica', to='licitacions.departament')),
                ('lloc_execucio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='licitacio_publica', to='licitacions.localitzacio')),
                ('organ', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='licitacio_publica', to='licitacions.organ')),
                ('tipus_contracte', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='licitacio_publica', to='licitacions.tipuscontracte')),
            ],
        ),
        migrations.CreateModel(
            name='LicitacioPrivada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procediment', models.CharField(choices=[('Obert', 'Obert'), ('Contracte menor', 'Contracte menor'), ('Negociat sense publicitat', 'Negociat sense publicitat'), ('Contracte basat en acord marc', 'Contracte basat en acord marc'), ('Altres procediments segons instruccions internes', 'Altres procediments segons instruccions internes'), ('Restringit', 'Restringit'), ('Específic de Sistema Dinàmic de Adquisició', 'Específic de Sistema Dinàmic de Adquisició'), ('Concurs de projectes', 'Concurs de projectes'), ('Contracte derivat de acord marc', 'Contracte derivat de acord marc'), ('Licitació amb negociació', 'Licitació amb negociació'), ('Negociat amb publicitat', 'Negociat amb publicitat')], max_length=150, null=True)),
                ('fase_publicacio', models.CharField(choices=[('Formalització', 'Formalització'), ('Adjudicació', 'Adjudicació'), ('Anunci de licitació en avaluació', 'Anunci de licitació en avaluació'), ('Adjudicació deserta', 'Adjudicació deserta'), ('Desistiment', 'Desistiment'), ('Anul·lació de expedient', 'Anul·lació de expedient'), ('Anunci de licitació en termini', 'Anunci de licitació en termini'), ('Encàrrec a mitjà pròpi', 'Encàrrec a mitjà pròpi'), ('Decisió de no adjudicar un contracte', 'Decisió de no adjudicar un contracte'), ('Alerta de futura licitació', 'Alerta de futura licitació'), ('Anunci previ', 'Anunci previ'), ('Decisió de no subscriure un contracte', 'Decisió de no subscriure un contracte')], max_length=80, null=True)),
                ('denominacio', models.TextField(null=True)),
                ('objecte_contracte', models.TextField(null=True)),
                ('pressupost', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('valor_estimat_contracte', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('duracio_contracte', models.CharField(max_length=80, null=True)),
                ('termini_presentacio_ofertes', models.DateTimeField(null=True)),
                ('data_publicacio_anunci', models.DateTimeField(null=True)),
                ('data_publicacio_adjudicacio', models.DateTimeField(null=True)),
                ('codi_cpv', models.IntegerField(null=True)),
                ('import_adjudicacio_sense_iva', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('import_adjudicacio_amb_iva', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('ofertes_rebudes', models.IntegerField(null=True)),
                ('resultat', models.CharField(max_length=50, null=True)),
                ('data_adjudicacio_contracte', models.DateField(null=True)),
                ('data_formalitzacio_contracte', models.DateField(null=True)),
                ('lloc_execucio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='licitacio_privada', to='licitacions.localitzacio')),
                ('tipus_contracte', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='licitacio_privada', to='licitacions.tipuscontracte')),
            ],
        ),
    ]
