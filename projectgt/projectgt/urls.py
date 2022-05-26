from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gtapp/', include('gtapp.urls')),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.views.generic import RedirectView

urlpatterns += [
    path('', RedirectView.as_view(url='gtapp/', permanent=True)),
]