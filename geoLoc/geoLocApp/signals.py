from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
import geoLocApp.models

import geoLocApp.distance

@receiver(pre_save,sender=geoLocApp.models.Coordonnee,dispatch_uid="only_before_registered")
def setDistance(sender, **kwargs):
    coordonnee = kwargs["instance"]
    position = coordonnee.position
    coordonnee.distance = geoLocApp.distance.distance(coordonnee.latitude,position.latitude,coordonnee.longitude,position.longitude)

@receiver(post_save,sender=geoLocApp.models.Position,dispatch_uid="new_position_added")
def new_position(sender,**kwargs):
    if kwargs['created']==True:
        return ['intance']
    else:
        return 0