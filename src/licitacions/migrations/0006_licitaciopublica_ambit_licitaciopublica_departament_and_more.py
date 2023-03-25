# Generated by Django 4.1.7 on 2023-03-25 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licitacions', '0005_tipuscontracte'),
    ]

    operations = [
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
    ]
