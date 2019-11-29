from django.contrib.auth.models import User,Group
from django.shortcuts import get_list_or_404,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets,permissions

from .serializers import CoordonneeModelSerializer,PositionModelSerializer,UserSerializer,GroupSerializer
from .models import Coordonnee,Position

from .distance import distance

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PositionViewSet(viewsets.ViewSet):
    """ """

    def list(self,request):
        """ """
        position_coordonnees = []

        request_data = []

        positions = get_list_or_404(Position)
        coordonnees = get_list_or_404(Coordonnee)
        for position in positions:
            for coordonnee in coordonnees:
                coordonnee.distance = distance(position.latitude,coordonnee.latitude,position.longitude,coordonnee.longitude)
            coordonnees = sorted(coordonnees, key=lambda coordonnee: coordonnee.distance,reverse=False)
            coordonnees_serialized = CoordonneeModelSerializer(coordonnees,many=True)
            position_serialized =  PositionModelSerializer(position)
            position_coordonnees.append(position_serialized.data)
            position_coordonnees.append(coordonnees_serialized.data)
        request_data.append(position_coordonnees)
        return Response(data=request_data)

    def create(self,request):
        """ Une implémentation de la requête POST . """

        position_identifiant = request.data[0]["identifiant"]
        qs =  Position.objects.filter(identifiant__iexact=position_identifiant)
        if not qs.exists():
            poserialized = PositionModelSerializer(data=request.data[0])
        else:
            poserialized = PositionModelSerializer(qs.first(),data=request.data[0])
        if poserialized.is_valid():
            position = poserialized.save()
            for coordonnee in request.data[1]:
                coordonnee["distance"] = distance(position.latitude,coordonnee['latitude'],position.longitude,coordonnee['longitude'])
                coordonnee_identifiant = coordonnee["identifiant"]
                qs =  Coordonnee.objects.filter(identifiant__iexact=coordonnee_identifiant)
                if not qs.exists():
                    coordserialized = CoordonneeModelSerializer(data=coordonnee)
                else:
                    coordonnee_instance = qs.first()
                    coordserialized = CoordonneeModelSerializer(coordonnee_instance,data=coordonnee)
                if not coordserialized.is_valid():
                    return Response(coordserialized.errors, status=status.HTTP_400_BAD_REQUEST)
                coordserialized.save()
            request.data[1] = sorted(request.data[1], key=lambda coordonnee: coordonnee['distance'],reverse=False)
            return Response(request.data,status=status.HTTP_201_CREATED)
        return Response(poserialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None,**kwargs):
        """ """
        pass

    def update(self,request,pk=None,**kwargs):
        """ """
        pass

    def partial_update(self,request,pk=None,**kwargs):
        """ """
        pass

    def destroy(self,request,pk=None,**kwargs):
        """ """
        pass