from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Coordonnee, Position


class CoordonneeModelSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Coordonnee
        fields = ['longitude','latitude','position','distance']

class PositionModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields =['longitude','latitude']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']

# class CoordonneeSerializer(serializers.Serializer):
#     longitude =  serializers.FloatField()
#     latitude = serializers.FloatField()
#     distance = serializers.ListField