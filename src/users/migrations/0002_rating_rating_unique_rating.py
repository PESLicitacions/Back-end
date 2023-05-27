# Generated by Django 4.1.7 on 2023-05-27 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_rated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rated', to=settings.AUTH_USER_MODEL)),
                ('user_who_rates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who_rates', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('user_who_rates', 'user_rated'), name='unique_rating'),
        ),
    ]
