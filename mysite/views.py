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
        yourid = request.GET['userId']
        yourpassword = request.GET['userPassword']
        urpasswordconfirm = request.GET['userPasswordConfirm']
        uremail = request.GET['userEmail']
        urage = request.GET['userAge']
        urgender = request.GET['userGender']
        ureducation = request.GET['userEducation']

    except:
        yourid = None
        message = 'Something wrong!'

    if yourid != None and yourpassword == urpasswordconfirm:
        accounts = models.Account.objects.create(account=yourid, password=yourpassword,
                                                 passwordConfirmation=urpasswordconfirm, email=uremail,
                                                 age=urage, gender=urgender, education=ureducation)
        accounts.save()

    return render(request, 'signup.html', locals())