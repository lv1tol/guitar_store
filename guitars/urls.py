from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)