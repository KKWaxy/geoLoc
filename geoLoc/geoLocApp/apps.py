from django.apps import AppConfig


class GeolocappConfig(AppConfig):
    name = 'geoLocApp'

    def ready(self):
        import geoLocApp.signals