from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse


def current_datetime(request):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse('Current Datetime: %s' % now)
