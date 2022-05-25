from django.urls import path
from .views import IndexView, ImagenView


app_name = 'gtapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('imagen/', ImagenView.as_view(), name='imagen'),
]