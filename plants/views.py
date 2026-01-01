from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import Plant,CareLog
from .forms import PlantForm
# Create your views here.
def plant_index(request):
    plants=Plant.objects.all()
    return render(request,'plant/index.html',{'plants':plants})

def plant_create(request):
    form = PlantForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        
    context = {'form': form}
    return render(request, 'plant/form.html', context)

def plant_delete(request):
    return HttpResponse('plant delete sayfası')

def plant_detail(request,id):
    plant=get_object_or_404(Plant, id=id) 
    carelogs= plant.care_logs.all()  #ilişkili bakım kayıtlarını al
    return render(request,'plant/detail.html',{'plant':plant,'carelogs':carelogs})

def plant_update(request):
    return HttpResponse('plant update sayfası')



