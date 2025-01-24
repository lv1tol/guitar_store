from django.shortcuts import render
from guitars.models import Guitar
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    guitars = Guitar.objects.all()
    return render(request, "index.html", {'guitars': guitars})

def catalog(request):
    guitars = Guitar.objects.all()
    return render(request, "catalog.html", {'guitars': guitars})

def details(request, id):
    guitars = Guitar.objects.all()
    return render(request, "details.html", {'guitars': guitars, 'id': id})

    def create(request):
        if request.method == "POST":
            form = GuitarForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('guitars:index'))
        else:
            form = GuitarForm()
        return render(request, "create.html", {'form': form})

    def update(request, id):
        guitar = Guitar.objects.get(pk=id)
        if request.method == "POST":
            form = GuitarForm(request.POST, instance=guitar)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('guitars:details', args=[id]))
        else:
            form = GuitarForm(instance=guitar)
        return render(request, "update.html", {'form': form, 'id': id})

def delete(request, id):
    guitar = Guitar.objects.get(pk=id)
    if request.method == "POST":
        guitar.delete()
        return HttpResponseRedirect(reverse('guitars:index'))
    return render(request, "delete.html", {'guitar': guitar})
