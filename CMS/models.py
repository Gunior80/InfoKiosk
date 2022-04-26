from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Index(models.Model):
    pos = models.PositiveIntegerField()
    name = models.CharField(name="Название")
    parent = models.ForeignKey("self", on_delete=models.CASCADE(), related_name="parent", )
    #app
    #material


class SimpleMaterial(models.Model):
    name = models.CharField(name="Название")
    content = HTMLField()