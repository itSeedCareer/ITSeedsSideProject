from django.shortcuts import render
from mysite import models

# Create your views here.

def index(request):
    try:
        urid = request.GET['userId']
        urpassword = request.GET['userPassword']
    except:
        urid = None
        message = 'Something wrong!'

    if urid != None:
        account = models.Test.objects.create(account=urid, password=urpassword)
        account.save()

    return render(request, 'index.html', locals())

def signUp(request):
    try:
        urid = request.GET['userId']
        urpassword = request.GET['userPassword']
    except:
        urid = None
        message = 'Something wrong!'

    if urid != None and urpassword == '12345':
        account = models.Account.objects.create(account=urid, password=urpassword)
        account.save()

    return render(request, 'signUp.html', locals())
