from django.shortcuts import render
from mysite import  models

# Create your views here.

def index(request):
    try:
        urId = request.GET['userId']
        urPassword = request.GET['userPassword']
    except:
        urId = None

    if urId != None and urPassword == '12345':
        verified = True
    else:
        verified = False
    return render(request, 'index.html', locals())
