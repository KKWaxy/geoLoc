# Generated by Django 2.2.7 on 2019-11-18 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoLocApp', '0007_auto_20191118_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordonnee',
            name='slug',
            field=models.SlugField(default='Rien', verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='position',
            name='slug',
            field=models.SlugField(default='Rien', verbose_name='Slug'),
        ),
    ]
