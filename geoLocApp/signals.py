from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
import geoLocApp.models

import geoLocApp.distance

# @receiver(post_save,sender=geoLocApp.models.Position,dispatch_uid="only_before_registered")
# def setDistance(sender, **kwargs):
#     position = kwargs["instance"]
#     coordonnees = position.coordonnees.all()
#     print(coordonnees)
#     for coordonnee in coordonnees:
#         coordonnee.distance = geoLocApp.distance.distance(coordonnee.latitude,position.latitude,coordonnee.longitude,position.longitude)
#         print(coordonnee.distance)

# @receiver(post_save,sender=geoLocApp.models.Position,dispatch_uid="new_position_added")
# def new_position(sender,**kwargs):
#     if kwargs['created']==True:
#         return ['intance']
#     else:
#         return 0