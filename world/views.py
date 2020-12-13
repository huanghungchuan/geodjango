from django.shortcuts import render
from django.http import JsonResponse
from googleplaces import GooglePlaces, types, lang
from .models import Locations

# Create your views here.
def updatedb(request):
    try:
        lat = request.POST['lat']
        lon = request.POST['lon']

        location = Locations()
        location.lat = lat
        location.lon = lon
        location.save()
        return JsonResponse({"message": 'Successfully updated'}, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)

def getPlaceType(placeType):
    switcher = {
        'restaurant': types.TYPE_RESTAURANT,
        'cafe': types.TYPE_CAFE,
        'museum': types.TYPE_MUSEUM,
        'atm': types.TYPE_ATM,
        'taxi': types.TYPE_TAXI_STAND,
        'library': types.TYPE_LIBRARY,
        'casino': types.TYPE_CASINO,
    }
    return switcher.get(placeType, "Invalid Argument")

def updatePlaceType(request):
    f = open ('KEY.txt', 'r')
    API_KEY = f.read()
    f.close()


    try:
        requestPlaceType = request.POST['type']
        currentLat = float(request.POST['lat'])
        currentLng = float(request.POST['lng'])

        names = []
        lat = []
        lng = []
        address = []
        google_places = GooglePlaces(API_KEY)
        if requestPlaceType == 'default':
            return
        
        query_result = google_places.nearby_search(
            lat_lng={'lat': currentLat, 'lng': currentLng}, keyword='Restaurants',
            radius=300, types=[getPlaceType(requestPlaceType)])
        
        for place in query_result.places:
            place.get_details()
            names.append(place.name)
            lat.append(float(place.geo_location['lat']))
            lng.append(float(place.geo_location['lng']))
            address.append(place.formatted_address)
        
        return JsonResponse({'names':names, 'lat':lat, 'lng':lng, 'address':address}, status=200, safe=False)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)