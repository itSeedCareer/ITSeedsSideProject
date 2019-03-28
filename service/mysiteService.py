from django.shortcuts import render, redirect
from mysite import models, forms
from django.contrib.sessions.models import Session


def mysite_login(request):
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
                    message = "Login Successfully !"
                    return redirect('/')
                else:
                    message = "Password wrong!"

            except:
                message = "User not find!"

        else:
            message = "Please check again!"

    else:
        login_form = forms.LoginForm()

    return render(request, 'mysite/login.html', locals())