# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('updatedb/', views.updatedb, name='updatedb'),
    path('updatePlaceType/', views.updatePlaceType, name='updatePlaceType'),
]