from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))
    
def bus_stations(request):
    path_bus_stations = settings.BUS_STATION_CSV
    with open(path_bus_stations, 'r', encoding='utf-8') as file:
        csv_data = csv.DictReader(file)
        bus_stations = [row for row in csv_data]
    paginator = Paginator(bus_stations, 10)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page,
        
    }
    return render(request, 'stations/index.html', context)
