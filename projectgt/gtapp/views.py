from django.http import HttpResponse
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

  
def palindromo(request):
    """Palindrome function"""
    if request.method == 'POST':
        palabra = request.POST.get('palabra', '')

        invertida = palabra[::-1]

        if invertida == palabra:
            return HttpResponse("Is Palindrome")
        else:
            return HttpResponse("Not is Palindrome")

    return render(request, 'games.html', )

def parorimpar(request):
    """Odd or even function"""

    if request.method == 'POST':
        num = request.POST.get('num', '')

        num = int(num)

        if num%2 == 0:
            return HttpResponse("It's Even")
        else:
            return HttpResponse("It's Odd")
            
    return render(request, 'games.html')