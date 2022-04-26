
from django.http import HttpResponse
from django.shortcuts import render

from InfoKiosk.settings import TEMPLATE


def index(request):
    return render(request, TEMPLATE+'base.html')