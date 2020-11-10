from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class MapView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('map')
    template_name = 'map/map.html'