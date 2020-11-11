from django.contrib.gis import admin
from .models import Locations, WorldBorder

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(Locations, admin.OSMGeoAdmin)