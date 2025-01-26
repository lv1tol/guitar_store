from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.forms import model_to_dict
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib import messages

from guitars.forms.create import GuitarCreateForm
from guitars.models import Guitar

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
    form = GuitarCreateForm()
    if request.method == "POST":
        form = GuitarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            print("in2")
            form.save()
            messages.success(request, "User created successfully!")
            return redirect("/")
        else:
            print("err")
            messages.error(request, "Invalid data!")
    return render(request, "create.html", {"form": form, "return_url": "/"})


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
