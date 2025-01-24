from django.urls import path

from guitars import views

urlpatterns = [
    path("", views.index),
    path("catalog/", views.catalog),
    path("details/<int:id>", views.details),
]