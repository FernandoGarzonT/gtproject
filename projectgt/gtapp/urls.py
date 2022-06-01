from django.urls import path
from .views import IndexView, ImagenView, palindromo, parorimpar


app_name = 'gtapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('imagen/', ImagenView.as_view(), name='imagen'),
    path('games/', parorimpar, name='games'),
    path('games/', palindromo, name='games'),
]