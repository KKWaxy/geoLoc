# Generated by Django 2.2.7 on 2019-11-17 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoLocApp', '0003_auto_20191117_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordonnee',
            name='nom',
            field=models.CharField(default='INDEFINIE', max_length=100, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='position',
            name='nom',
            field=models.CharField(default='INDEFINIE', max_length=100, verbose_name='Nom'),
        ),
    ]
