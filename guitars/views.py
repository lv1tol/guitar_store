from django.shortcuts import render

from guitars.models import Guitar
# Create your views here.

def index(request):
    guitars = Guitar.objects.all()
    return render(request, "index.html", {'guitars': guitars})

def catalog(request):
    return render(request, "catalog.html", {})

def details(request, id):
    return render(request, "details.html", {"id": id})