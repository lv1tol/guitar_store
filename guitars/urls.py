from django.urls import path

from guitars import views

urlpatterns = [
    path("", views.catalog),
    path("all/", views.index),
    path("catalog/", views.catalog),
    path("delete/<int:id>", views.delete),
    path("update/<int:id>", views.update),
    path("createGuitar/", views.create),
    path("details/<int:id>", views.details),
]