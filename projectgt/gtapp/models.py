from distutils.command.upload import upload
from django.db import models

class Imagen(models.Model):
    """Create Model Imagen"""

    name_imagen = models.CharField(max_length=50, help_text='Name description')
    image_location = models.ImageField(upload_to='images/', blank=True, null=True)
    text_imagen = models.TextField(max_length=10000)
    date_create_imagen = models.DateTimeField('Date Create Imagen')

    def __str__(self):
        return self.name_imagen
        