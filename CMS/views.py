import json

from django.views import View
from django.views.decorators.csrf import csrf_exempt

from . import models
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse, HttpResponseServerError

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


@csrf_exempt
def getIndexes(request):
    indexes = models.Index.objects.filter(parent__isnull=True,
                                          content__isnull=False).order_by('pos').values('name', 'pos')
    data = json.dumps(list(indexes))
    return HttpResponse(data, content_type="application/json")


@csrf_exempt
def getSubIndexes(request):
    if request.method == "POST":
        if request.is_ajax():
            print()
    else:

    print(request.body)
    json_data = json.loads(request.body)
    try:
        data = json_data['data']
        print(data)
    except KeyError:
        HttpResponseServerError("Malformed data!")
    HttpResponse("Got json data")
