from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from models import House

# Create your views here.

def sms(request):
    return render(request, 'sms\sms.html', {})

def houses(request):
    all_houses = House.objects[:10]
    output = ', '.join([h.name for h in all_houses])
    return HttpResponse(output)

def housesGroup(request, house_id):
    return HttpResponse("<h1>Viewing House: %s with id %s </h1>" % (House.name, house_id))
