from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from models import Student
from models import House

# Create your views here.

def sms(request):
    return render(request, 'sms\sms.html', {})

def houses(request):
    all_houses = House.objects.all()
    output = [h.name for h in all_houses]
    return render(request, 'sms\houses.html', {'output' : output})

class StudentList(ListView):
    model = Student
    context_object_name = 'students'
