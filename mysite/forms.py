from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label="User Name", max_length=10)
    user_password =forms.CharField(label="User Password", widget=forms.PasswordInput())
    