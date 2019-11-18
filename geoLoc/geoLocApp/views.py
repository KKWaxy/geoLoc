from django.contrib.auth.models import User,Group
from django.shortcuts import get_list_or_404,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from .serializers import UserSerializer,GroupSerializer,CoordonneeModelSerializer,PositionModelSerializer
from .models import Coordonnee,Position


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CoordonneeListView(APIView):

    """ Il s'agit d'une liste de cordonnées avec comme tête de liste une Position."""


    def get(self,request,format=None,position_slug=None):
        if position_slug == None:
            position = get_list_or_404(Position)[0]
        else:
            position = get_object_or_404(Position,slug=position_slug.lower())
        coordonnees = get_list_or_404(Coordonnee,position=position)
        #On fait le tri suivant la distance
        coordonnees = sorted(coordonnees, key=lambda coordonnee: coordonnee.distance,reverse=False)
        
        positionSerializer = PositionModelSerializer(position)
        positionSerialiser = [positionSerializer.data]
        coordonneeSerializer = CoordonneeModelSerializer(coordonnees,many=True)
        serializer  = positionSerialiser + coordonneeSerializer.data

        
        return (Response(data=serializer))

    def post(self,request,format=None):
        """ Nous testons pour voir si la serialisation s'est bien dérouléé avant de l'enregistrer."""

        poserialized = PositionModelSerializer(data=request.data[0])
        if poserialized.is_valid():
            poserialized.save()
            try:
                new_position = Position.objects.all()[0]
            except Position.DoesNotExist as identifier:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            for coordonnee in request.data[1::]:
                coordonnee["position"] = new_position.pk
            coordserialized = CoordonneeModelSerializer(data=request.data[1::],many=True)
            if coordserialized.is_valid():
                coordserialized.save()
                return Response(request.data,status=status.HTTP_201_CREATED)
            else:
                return Response(coordserialized.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(poserialized.errors, status=status.HTTP_400_BAD_REQUEST)