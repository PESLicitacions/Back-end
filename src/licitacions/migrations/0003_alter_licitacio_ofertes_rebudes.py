# Generated by Django 4.1.7 on 2023-05-30 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licitacions', '0002_licitacio_num_favorits_licitacio_visualitzacions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licitacio',
            name='ofertes_rebudes',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
