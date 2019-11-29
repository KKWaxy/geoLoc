from datetime import datetime,timedelta
import random

from django.db import models
from django.utils.translation import gettext as _
from django.utils.timezone import timezone

DEFAULT_POSITION_NAME = u"INDEFINIE"
DEFAULT_ID = random.randint(random.randint(12,100000),random.randint(92,1000000)*12)
class AbstractCoord(models.Model):
    """ """
    identifiant = models.IntegerField(_('Identifiant'), unique = True, default = DEFAULT_ID, help_text="Ce identifiant doit de venir de la requête POST.")
    nom = models.CharField(_("Nom"),max_length=100,default=DEFAULT_POSITION_NAME)
    slug = models.SlugField(_('Slug'),null=True,blank=True)
    longitude =  models.FloatField(_("Longitute :"))
    latitude = models.FloatField(_("Latitude :"))
    create_date = models.DateTimeField("Date de la requete",auto_now_add=True)
    
    class Meta:

        abstract = True

    def __str__(self):
        return self.nom


class Coordonnee(AbstractCoord):
   """ """
   
   distance = models.FloatField(_("Distance :"),null=True,blank=True)

   class Meta:
       ordering = ("-distance",)


class Position(AbstractCoord):
    """ """
    class Meta:
        ordering = ('-create_date',)
