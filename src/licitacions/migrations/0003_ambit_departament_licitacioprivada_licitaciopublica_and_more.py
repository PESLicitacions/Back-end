# Generated by Django 4.1.7 on 2023-03-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licitacions', '0002_localitzacio_alter_licitacio_procediment'),
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
            name='LicitacioPrivada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procediment', models.CharField(choices=[('Obert', 'Obert'), ('Contracte menor', 'Contracte menor'), ('Negociat sense publicitat', 'Negociat sense publicitat'), ('Contracte basat en acord marc', 'Contracte basat en acord marc'), ('Altres procediments segons instruccions internes', 'Altres procediments segons instruccions internes'), ('Restringit', 'Restringit'), ('Específic de Sistema Dinàmic de Adquisició', 'Específic de Sistema Dinàmic de Adquisició'), ('Concurs de projectes', 'Concurs de projectes'), ('Contracte derivat de acord marc', 'Contracte derivat de acord marc'), ('Licitació amb negociació', 'Licitació amb negociació'), ('Negociat amb publicitat', 'Negociat amb publicitat')], max_length=150)),
                ('fase_publicacio', models.CharField(choices=[('Formalització', 'Formalització'), ('Adjudicació', 'Adjudicació'), ('Anunci de licitació en avaluació', 'Anunci de licitació en avaluació'), ('Adjudicació deserta', 'Adjudicació deserta'), ('Desistiment', 'Desistiment'), ('Anul·lació de expedient', 'Anul·lació de expedient'), ('Anunci de licitació en termini', 'Anunci de licitació en termini'), ('Encàrrec a mitjà pròpi', 'Encàrrec a mitjà pròpi'), ('Decisió de no adjudicar un contracte', 'Decisió de no adjudicar un contracte'), ('Alerta de futura licitació', 'Alerta de futura licitació'), ('Anunci previ', 'Anunci previ'), ('Decisió de no subscriure un contracte', 'Decisió de no subscriure un contracte')], max_length=80)),
                ('denominacio', models.TextField()),
                ('objecte_contracte', models.TextField()),
                ('pressupost', models.DecimalField(decimal_places=2, max_digits=9)),
                ('valor_estimat_contracte', models.DecimalField(decimal_places=2, max_digits=9)),
                ('duracio_contracte', models.CharField(max_length=80)),
                ('termini_presentacio_ofertes', models.DateTimeField()),
                ('data_publicacio_anunci', models.DateTimeField()),
                ('data_publicacio_adjudicacio', models.DateTimeField()),
                ('codi_cpv', models.IntegerField()),
                ('import_adjudicacio_sense_iva', models.DecimalField(decimal_places=2, max_digits=9)),
                ('import_adjudicacio_amb_iva', models.DecimalField(decimal_places=2, max_digits=9)),
                ('ofertes_rebudes', models.IntegerField()),
                ('resultat', models.CharField(max_length=50)),
                ('data_adjudicacio_contracte', models.DateField()),
                ('data_formalitzacio_contracte', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LicitacioPublica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procediment', models.CharField(choices=[('Obert', 'Obert'), ('Contracte menor', 'Contracte menor'), ('Negociat sense publicitat', 'Negociat sense publicitat'), ('Contracte basat en acord marc', 'Contracte basat en acord marc'), ('Altres procediments segons instruccions internes', 'Altres procediments segons instruccions internes'), ('Restringit', 'Restringit'), ('Específic de Sistema Dinàmic de Adquisició', 'Específic de Sistema Dinàmic de Adquisició'), ('Concurs de projectes', 'Concurs de projectes'), ('Contracte derivat de acord marc', 'Contracte derivat de acord marc'), ('Licitació amb negociació', 'Licitació amb negociació'), ('Negociat amb publicitat', 'Negociat amb publicitat')], max_length=150)),
                ('fase_publicacio', models.CharField(choices=[('Formalització', 'Formalització'), ('Adjudicació', 'Adjudicació'), ('Anunci de licitació en avaluació', 'Anunci de licitació en avaluació'), ('Adjudicació deserta', 'Adjudicació deserta'), ('Desistiment', 'Desistiment'), ('Anul·lació de expedient', 'Anul·lació de expedient'), ('Anunci de licitació en termini', 'Anunci de licitació en termini'), ('Encàrrec a mitjà pròpi', 'Encàrrec a mitjà pròpi'), ('Decisió de no adjudicar un contracte', 'Decisió de no adjudicar un contracte'), ('Alerta de futura licitació', 'Alerta de futura licitació'), ('Anunci previ', 'Anunci previ'), ('Decisió de no subscriure un contracte', 'Decisió de no subscriure un contracte')], max_length=80)),
                ('denominacio', models.TextField()),
                ('objecte_contracte', models.TextField()),
                ('pressupost', models.DecimalField(decimal_places=2, max_digits=9)),
                ('valor_estimat_contracte', models.DecimalField(decimal_places=2, max_digits=9)),
                ('duracio_contracte', models.CharField(max_length=80)),
                ('termini_presentacio_ofertes', models.DateTimeField()),
                ('data_publicacio_anunci', models.DateTimeField()),
                ('data_publicacio_adjudicacio', models.DateTimeField()),
                ('codi_cpv', models.IntegerField()),
                ('import_adjudicacio_sense_iva', models.DecimalField(decimal_places=2, max_digits=9)),
                ('import_adjudicacio_amb_iva', models.DecimalField(decimal_places=2, max_digits=9)),
                ('ofertes_rebudes', models.IntegerField()),
                ('resultat', models.CharField(max_length=50)),
                ('data_adjudicacio_contracte', models.DateField()),
                ('data_formalitzacio_contracte', models.DateField()),
                ('enllaç', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('codi', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100, verbose_name='nom organ')),
            ],
        ),
        migrations.DeleteModel(
            name='Licitacio',
        ),
        migrations.RemoveField(
            model_name='localitzacio',
            name='id',
        ),
        migrations.AlterField(
            model_name='localitzacio',
            name='nom',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
