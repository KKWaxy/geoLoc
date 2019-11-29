from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Coordonnee, Position


class CoordonneeModelSerializer(serializers.ModelSerializer):    
    """ """
    distance = serializers.FloatField(default=0)
    class Meta:
        
        model = Coordonnee
        fields = ['identifiant','nom','longitude','latitude','distance']

    # def validate_identifiant(self,value):
        

class PositionModelSerializer(serializers.ModelSerializer):
    """ """

    class Meta:
        model = Position
        fields = ['identifiant','nom','longitude','latitude']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url','username','email','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']
