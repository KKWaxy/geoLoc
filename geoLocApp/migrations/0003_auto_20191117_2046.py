# Generated by Django 2.2.7 on 2019-11-17 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoLocApp', '0002_auto_20191117_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordonnee',
            name='nom',
            field=models.CharField(default='Coordonnee', max_length=100, verbose_name='Nom'),
        ),
        migrations.AddField(
            model_name='position',
            name='nom',
            field=models.CharField(default='Coordonnee', max_length=100, verbose_name='Nom'),
        ),
    ]
