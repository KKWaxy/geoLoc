from django.urls import path,include

from rest_framework import routers

from .views import PositionViewSet,UserViewSet,GroupViewSet

app_name ='geoLocApp'

router =  routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'groups',GroupViewSet)
router.register(r'coordonnees',PositionViewSet,base_name='coordonnees')

urlpatterns = [
    path('',include(router.urls)),
]