# Generated by Django 4.1.7 on 2023-05-01 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('licitacions', '0004_listafavorits_listafavorits_unique_favorits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipus_contracte', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preference', to='licitacions.tipuscontracte')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preference', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='preference',
            constraint=models.UniqueConstraint(fields=('user', 'tipus_contracte'), name='unique_preference'),
        ),
    ]
