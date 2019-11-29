from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
import geoLocApp


urlpatterns = [
    path('',include('geoLocApp.urls',namespace="geoLocApp")), 
    path('admin/', admin.site.urls)   
]

# This part permit to add login to the Browsable API
urlpatterns += [
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
