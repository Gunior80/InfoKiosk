from django.contrib import admin

# Register your models here.
from CMS.models import Index, SimpleMaterial


class IndexModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'pos',]

admin.site.register(Index, IndexModelAdmin)

admin.site.register(SimpleMaterial)