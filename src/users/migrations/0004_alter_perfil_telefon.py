# Generated by Django 4.1.7 on 2023-04-30 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_perfil_cif_alter_perfil_telefon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='telefon',
            field=models.TextField(),
        ),
    ]
