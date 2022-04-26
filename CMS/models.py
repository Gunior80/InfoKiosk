from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from positions import PositionField
from tinymce.models import HTMLField
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Index(MPTTModel):
    name = models.CharField(verbose_name="Название", max_length=64)
    parent = TreeForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Родительский элемент")
    pos = PositionField(collection='parent')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name


class SimpleMaterial(models.Model):
    name = models.CharField(verbose_name="Название", max_length=64)
    content = HTMLField(verbose_name="Материал")

    def __str__(self):
        return self.name
