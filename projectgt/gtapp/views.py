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


class GamesView(generic.ListView):
    template_name = 'games.html'
    context_object_name= 'context_game'

    def parorimpar(request):
        """Odd or even function"""

        if request.method == 'POST':
            num = int(input("Escribe un Numero: "))

            if num%2 == 0:
                print(f"{num} Es Par")
            else:
                print(f"{num} Es Impar")
        
        return render(request, 'gtapp/games.html', {'title':'games'})


    def palindromo(request):
        """Game Palindromo"""

        palabra = input("Escribe una palabra: ").upper()

        invertida = palabra[::-1].lower()

        if invertida == palabra:
            print(f"{palabra} - {invertida} Es un Palindromo")
        else:
            print(f"{palabra} - {invertida} No es un Palindromo")
        
        return render(request, 'gtapp/games.html', {'title':'games'})
    
    def get_queryset(self):
        return 