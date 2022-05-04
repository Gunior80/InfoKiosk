from django.contrib import admin
from django.contrib.auth.models import User, Group

from CMS.models import Index, Content

admin.site.unregister(User)
admin.site.unregister(Group)

class IndexModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'pos', 'content']
    exclude = ['parent',]
admin.site.register(Index, IndexModelAdmin)

class ContentModelAdmin(admin.ModelAdmin):
    list_display = ['name', ]

admin.site.register(Content, ContentModelAdmin)