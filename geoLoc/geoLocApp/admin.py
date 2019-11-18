from django.contrib import admin

# Register your models here.
from .models import Position,Coordonnee

admin.site.register(Position)
admin.site.register(Coordonnee)