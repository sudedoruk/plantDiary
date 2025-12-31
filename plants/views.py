from django.shortcuts import render, HttpResponse
from .models import Plant
# Create your views here.
def plant_index(request):
    plants=Plant.objects.all()
    return render(request,'plant/index.html',{'plants':plants})

def plant_create(request):
    return HttpResponse('plant create sayfası')

def plant_delete(request):
    return HttpResponse('plant delete sayfası')

def plant_detail(request):
    return HttpResponse('plant detail sayfası')

def plant_update(request):
    return HttpResponse('plant update sayfası')



