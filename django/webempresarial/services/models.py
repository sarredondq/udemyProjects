from django.db import models

# Create your models here.

# https://docs.djangoproject.com/en/2.0/ref/models/fields/


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="titulo")
    subtitle = models.CharField(max_length=200, verbose_name="subtitulo")
    content = models.TextField(verbose_name="contenido")
    image = models.ImageField(verbose_name="imagen", upload_to="services")# para guardarlo en esta carpeta / crea esta carpeta
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de edicion")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"]

    def __str__(self):
        return self.title
