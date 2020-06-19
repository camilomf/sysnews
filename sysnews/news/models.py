from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=45, verbose_name="Nombre", unique=True)
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    state = models.BooleanField(verbose_name="Estado", default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ['-created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/"

class Country(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    country_cod = models.CharField(max_length=200, verbose_name="Codpais", null=True, blank=True)
    description = models.TextField(max_length=100, verbose_name="Descripción", null=True, blank=True)
    state = models.BooleanField(verbose_name="Estado", default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=45, unique=True, verbose_name="Nombre")
    description = models.TextField(max_length=100, verbose_name="Descripción", null=True, blank=True)
    state = models.BooleanField(verbose_name="Estado", default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "fuente"
        verbose_name_plural = "fuentes"
        ordering = ['-created']

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return "/"


class News(models.Model):
    url = models.CharField(max_length=400, verbose_name="URL Principal")
    title = models.CharField(max_length=400, verbose_name="Titulo")
    headline = models.TextField(verbose_name="Encabezado", null=True, blank=True)
    explanation = models.TextField(verbose_name="Cuerpo")
    publication_date = models.DateField(verbose_name="Fecha de publicación", null=True, blank=True)
    tags = models.ManyToManyField(Tags, verbose_name="Tags")
    image = models.ImageField(upload_to='imagenes/')
    source = models.ForeignKey(Source, verbose_name="Fuente", on_delete=models.CASCADE)
    editor = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    country = models.ForeignKey(Country, verbose_name="Pais", on_delete=models.CASCADE)
    state = models.BooleanField(verbose_name="Estado", default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-created']

    def __str__(self):
        return self.title