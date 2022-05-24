# Generated by Django 4.0.4 on 2022-05-24 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_imagen', models.CharField(help_text='Name description', max_length=50)),
                ('image_location', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('text_imagen', models.TextField(max_length=10000)),
                ('date_create_imagen', models.DateTimeField(verbose_name='Date Create Imagen')),
            ],
        ),
    ]
