# Generated by Django 2.2.7 on 2019-11-29 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoLocApp', '0010_remove_position_coordonnees'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordonnee',
            name='identifiant',
            field=models.IntegerField(default=1684995, help_text='Ce identifiant doit de venir de la requête POST.', unique=True, verbose_name='Identifiant'),
        ),
        migrations.AddField(
            model_name='position',
            name='identifiant',
            field=models.IntegerField(default=1684995, help_text='Ce identifiant doit de venir de la requête POST.', unique=True, verbose_name='Identifiant'),
        ),
    ]
