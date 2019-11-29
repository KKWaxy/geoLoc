# from geoLocApp.distance import distance

# class Position(object):
#     def __init__(self,longitude,latitude):
#         self.longitude = longitude
#         self.latitude = latitude    

# class Coordonnee(object):
#     def __init__(self,distance=None, **kwargs):
#         self.distance = distance
#         super.__init__(self,**kwargs)

#     def setDistance(self,instance) -> int:
#         assert isinstance(instance,Position),f"TypeError:{instance} is not type of Positon."
#         self.distance = distance(self.latitude, instance.latitude, self.longitude, instance.longitude)
#         return 0