from django.shortcuts import render
from django.views import generic
from .models import Imagen


class IndexView(generic.ListView):
    template_name = 'index.html'
    model = Imagen

    def get_queryset(self):
        return Imagen.objects.all()


class ImagenView(generic.ListView):
    model = Imagen
    template_name = 'imagen.html'
    context_object_name= 'context_imagen'

    def get_queryset(self):
        return Imagen.objects.all()

