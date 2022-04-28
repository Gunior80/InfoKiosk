from . import models
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from InfoKiosk.settings import TEMPLATE


class Index(TemplateView):
    template_name = TEMPLATE+"index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['indexes'] = models.Index.objects.filter(parent__isnull=True, content__isnull=False).order_by('pos')
        if 'index' in context:
            context['content'] = models.Index.objects.get(pk=context['index']).content
        else:
            try:
                context['content'] = context['indexes'].first().content
            except:
                context['content'] = ""
        return context
