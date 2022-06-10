from django.urls import path
from .views import IndexView, ImagenView, GameView, RegistrationView, ProfileView
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'gtapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('imagen/', ImagenView.as_view(), name='imagen'),
    path('games/', GameView.as_view(), name='games'),
    path('login/', LoginView.as_view(template_name = 'login.html'), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]