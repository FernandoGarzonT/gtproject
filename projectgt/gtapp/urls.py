from django.urls import path
from .views import IndexView


appname = 'gtapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]