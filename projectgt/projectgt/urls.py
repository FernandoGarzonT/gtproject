from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gtapp/', include('gtapp.urls')),
]


from django.views.generic import RedirectView

urlpatterns += [
    path('', RedirectView.as_view(url='gtapp/', permanent=True)),
]