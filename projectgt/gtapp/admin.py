from django.contrib import admin
from .models import Imagen


@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('name_imagen', 'date_create_imagen')
    list_filter = ['date_create_imagen']
    search_fields = ['name_imagen']