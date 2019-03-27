from django.shortcuts import render, redirect
from mysite import models, forms


# Create your views here.

def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST['user_name']
            userpassword = request.POST['user_password']
            message = "Login Successfully !"
        else:
            message = "Not Success"

    else:
        login_form = forms.LoginForm()

    try:
        if username: request.session['username'] = username
        if userpassword: request.session['userpassword'] = userpassword
    except:
        pass

    return render(request, 'login.html', locals())

def signUp(request):
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

    return render(request, 'signup.html', locals())

def home(request):
    return render(request, 'home.html', locals())

def index(request):
    if 'username' in request.session:
        username = request.session['username']
        userpassword = request.session['userpassword']

    return render(request, 'home.html', locals())

def logout(request):
    request.session['username'] = None
    return redirect('/')
