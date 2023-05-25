# Generated by Django 4.1.7 on 2023-05-25 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='Licitacio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacio', models.TextField(null=True)),
                ('objecte_contracte', models.TextField(null=True)),
                ('pressupost', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
                ('valor_estimat_contracte', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
                ('duracio_contracte', models.IntegerField(null=True)),
                ('data_inici', models.DateField(null=True)),
                ('data_fi', models.DateField(null=True)),
                ('termini_presentacio_ofertes', models.DateTimeField(null=True)),
                ('data_publicacio_anunci', models.DateTimeField(null=True)),
                ('data_publicacio_adjudicacio', models.DateTimeField(null=True)),
                ('import_adjudicacio_sense_iva', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
                ('import_adjudicacio_amb_iva', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
                ('ofertes_rebudes', models.IntegerField(null=True)),
                ('resultat', models.CharField(max_length=50, null=True)),
                ('data_adjudicacio_contracte', models.DateField(null=True)),
                ('data_formalitzacio_contracte', models.DateField(null=True)),
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
            name='PreferencePressupost',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='preference_pressupost', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('pressupost_min', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
                ('pressupost_max', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PreferenceTipusLicitacio',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='preference_tipus_licitacio', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('privades', models.BooleanField(default=False)),
                ('publiques', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LicitacioPrivada',
            fields=[
                ('licitacio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='licitacions.licitacio')),
            ],
            bases=('licitacions.licitacio',),
        ),
        migrations.CreateModel(
            name='LicitacioPublica',
            fields=[
                ('licitacio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='licitacions.licitacio')),
                ('procediment', models.CharField(choices=[('Obert', 'Obert'), ('Contracte menor', 'Contracte menor'), ('Negociat sense publicitat', 'Negociat sense publicitat'), ('Contracte basat en acord marc', 'Contracte basat en acord marc'), ('Altres procediments segons instruccions internes', 'Altres procediments segons instruccions internes'), ('Restringit', 'Restringit'), ('Específic de Sistema Dinàmic de Adquisició', 'Específic de Sistema Dinàmic de Adquisició'), ('Concurs de projectes', 'Concurs de projectes'), ('Contracte derivat de acord marc', 'Contracte derivat de acord marc'), ('Licitació amb negociació', 'Licitació amb negociació'), ('Negociat amb publicitat', 'Negociat amb publicitat')], max_length=150, null=True)),
                ('fase_publicacio', models.CharField(choices=[('Formalització', 'Formalització'), ('Adjudicació', 'Adjudicació'), ('Anunci de licitació en avaluació', 'Anunci de licitació en avaluació'), ('Adjudicació deserta', 'Adjudicació deserta'), ('Desistiment', 'Desistiment'), ('Anul·lació de expedient', 'Anul·lació de expedient'), ('Anunci de licitació en termini', 'Anunci de licitació en termini'), ('Encàrrec a mitjà pròpi', 'Encàrrec a mitjà pròpi'), ('Decisió de no adjudicar un contracte', 'Decisió de no adjudicar un contracte'), ('Alerta de futura licitació', 'Alerta de futura licitació'), ('Anunci previ', 'Anunci previ'), ('Decisió de no subscriure un contracte', 'Decisió de no subscriure un contracte')], max_length=80, null=True)),
                ('codi_cpv', models.CharField(max_length=200, null=True)),
                ('enllaç', models.URLField(null=True)),
            ],
            bases=('licitacions.licitacio',),
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
            name='PreferenceTipusContracte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipus_contracte', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preference_tipus_contracte', to='licitacions.tipuscontracte')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preference_tipus_contracte', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PreferenceAmbit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ambit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preference_ambit', to='licitacions.ambit')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preference_ambit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListaFavorits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notificacions', models.BooleanField(default=False)),
                ('licitacio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorits', to='licitacions.licitacio')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='licitacio',
            name='lloc_execucio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='licitacio', to='licitacions.localitzacio'),
        ),
        migrations.AddField(
            model_name='licitacio',
            name='tipus_contracte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='licitacio', to='licitacions.tipuscontracte'),
        ),
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motiu', models.TextField(null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidatura', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='preferencetipuscontracte',
            constraint=models.UniqueConstraint(fields=('user', 'tipus_contracte'), name='unique_preference_tipus_contracte'),
        ),
        migrations.AddConstraint(
            model_name='preferenceambit',
            constraint=models.UniqueConstraint(fields=('user', 'ambit'), name='unique_preference_ambit'),
        ),
        migrations.AddConstraint(
            model_name='listafavorits',
            constraint=models.UniqueConstraint(fields=('user', 'licitacio'), name='unique_favorits'),
        ),
        migrations.AddField(
            model_name='licitaciopublica',
            name='ambit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='licitacio_publica', to='licitacions.ambit'),
        ),
        migrations.AddField(
            model_name='licitaciopublica',
            name='departament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='licitacio_publica', to='licitacions.departament'),
        ),
        migrations.AddField(
            model_name='licitaciopublica',
            name='organ',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='licitacio_publica', to='licitacions.organ'),
        ),
        migrations.AddField(
            model_name='licitacioprivada',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='licitacio_privada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='candidatura',
            name='licitacio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidatura', to='licitacions.licitacioprivada'),
        ),
        migrations.AddConstraint(
            model_name='candidatura',
            constraint=models.UniqueConstraint(fields=('user', 'licitacio'), name='unique_candidatura'),
        ),
    ]
