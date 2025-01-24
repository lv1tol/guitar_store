from django.shortcuts import render

from guitars.models import Guitar
# Create your views here.

def index(request):
    guitars = Guitar.objects.all()
    return render(request, "index.html", {'guitars': guitars})

def catalog(request):
    guitars = Guitar.objects.all()
    return render(request, "catalog.html", {'guitars': guitars})

def details(request, id):
    guitars = Guitar.objects.all()
    return render(request, "details.html", {'guitars': guitars, 'id': id})

