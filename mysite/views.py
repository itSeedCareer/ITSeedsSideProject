from django.shortcuts import render, redirect
from mysite import models, forms
from django.contrib.sessions.models import Session
from django.core.mail import EmailMessage
from django.contrib import messages


# Create your views here.

def login(request): # 登入函數

    #mysiteService.mysite_login()
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['user_name'].strip()
            login_password = request.POST['user_password']

            try:
                user = models.User.objects.get(name=login_name)
                if user.password == login_password:
                    request.session['username'] = user.name
                    request.session['useremail'] = user.email
                    messages.add_messag(request, messages.SUCCESS, "Success!")
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, "Password wrong!")

            except:
                messages.add_message(request, messages.WARNING, "User not find!")

        else:
            messages.add_message(request, messages.INFO, "Please check again!")

    else:
        login_form = forms.LoginForm()

    return render(request, 'mysite/login.html', locals())

def signup(request):
    try:
        yourid = request.POST['userId']
        yourpassword = request.POST['userPassword']
        urpasswordconfirm = request.POST['userPasswordConfirm']
        uremail = request.POST['userEmail']
        urage = request.POST['userAge']
        urgender = request.POST['userGender']
        ureducation = request.POST['userEducation']

    except:
        yourid = None
        message = 'Something wrong!'

    if yourid != None and yourpassword == urpasswordconfirm:
        accounts = models.Account.objects.create(account=yourid, password=yourpassword,
                                                 passwordConfirmation=urpasswordconfirm, email=uremail,
                                                 age=urage, gender=urgender, education=ureducation)
        accounts.save()

    return render(request, 'mysite/signup.html', locals())

def home(request):
    return render(request, 'mysite/home.html', locals())

def index(request, pid=None, del_pass=None): # 讀取session函數
    if 'username' in request.session:
        username = request.session['username']
        useremail = request.session['useremail']

    return render(request, 'mysite/home.html', locals())

def logout(request): # 登出函數
    if 'username' in request.session:
        Session.objects.all().delete()
        return redirect('/login/')
    return redirect('/')

def userinfo(request):
    if 'username' in request.session:
        username = request.session['username']
    else:
        return redirect('/login/')
    try:
        userinfo = models.User.objects.get(name=username)
    except:
        pass
    return render(request, 'mysite/userinfo.html', locals())


