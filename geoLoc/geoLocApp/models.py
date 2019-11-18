from datetime import datetime,timedelta

from django.db import models
from django.utils.translation import gettext as _
from django.utils.timezone import timezone


DEFAULT_POSITION_NAME = u"INDEFINIE"

class AbstractCoord(models.Model):

    nom = models.CharField(_("Nom"),max_length=100,default=DEFAULT_POSITION_NAME)
    longitude =  models.FloatField(_("Longitute :"))
    latitude = models.FloatField(_("Latitude :"))
    slug = models.SlugField(_('Slug'),default="Rien")
    create_date = models.DateTimeField("Date de la requete",auto_now_add=True)
    

    class Meta:

        abstract = True

    def __str__(self):
        return self.nom
    
class Position(AbstractCoord):
    class Meta:
        ordering = ('-create_date',)


class Coordonnee(AbstractCoord):

    position = models.ForeignKey(Position,on_delete = models.CASCADE)
    distance = models.FloatField(_("Distance :"),default=0)
    
    
    class Meta:
        ordering = ("-distance",)
        
