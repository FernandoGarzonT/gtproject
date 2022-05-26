from django.urls import path
from .views import IndexView, ImagenView, GamesView


app_name = 'gtapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('imagen/', ImagenView.as_view(), name='imagen'),
    path('games/', GamesView.as_view(), name='games'),
]