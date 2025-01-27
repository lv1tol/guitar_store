from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.forms import model_to_dict
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib import messages

from guitars.forms.create import GuitarCreateForm
from guitars.forms.update import GuitarUpdateForm
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
            form.save()
            messages.success(request, "Guitar added successfully!")
            return redirect("/")
        else:
            messages.error(request, "Invalid data!")
    return render(request, "create.html", {"form": form, "id": id})


def update(request, id):
    guitar = Guitar.objects.get(id=id)

    if guitar is None:
        return HttpResponse("User not found")

    form = GuitarUpdateForm(instance=guitar)

    if request.method == "POST":
        form = GuitarCreateForm(request.POST, request.FILES, instance=guitar)

        if request.FILES and guitar.avatar:
            guitar.avatar.delete()

        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, "update.html", {"form": form, "return_url": "/"})

def delete(request, id):
    guitar = Guitar.objects.get(pk=id)
    if guitar is None:
        return HttpResponse("Guitar not found")
    guitar.delete()
    return redirect("/")
