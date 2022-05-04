from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from positions import PositionField
from tinymce.models import HTMLField
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Content(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=64)
    content = HTMLField(verbose_name=_("Content"))

    class Meta:
        verbose_name = _("Content")
        verbose_name_plural = _("Contents")

    def __str__(self):
        return self.name


class Index(MPTTModel):
    name = models.CharField(verbose_name=_("Name"), max_length=64)
    parent = TreeForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL,
                            related_name='children', verbose_name=_("Parent index"))
    pos = PositionField(collection='parent', verbose_name=_("Position"))
    content = models.ForeignKey(Content, blank=True, null=True, on_delete=models.SET_NULL,
                                related_name="index", verbose_name=_("Content"))

    class MPTTMeta:
        order_insertion_by = ['pos']

    class Meta:
        verbose_name = _("Index")
        verbose_name_plural = _("Indexes")

    def __str__(self):
        return self.name

    def get_first(self):
        return Index.objects.get

    def get_childrens(self):
        return self.children.filter(content__isnull=False).order_by('pos')



# 1) Cначала, реализовать то, что выше. в двух типах шаблонов (с общим меню и с переходом на подстраницы)
# 2) Разобраться с кроссязыками.
# 3) Добавить функционал опроса.
# 4) Добавить функционал календаря с событиями.
# 5) Добавить генерацию ссылок на материалы.



