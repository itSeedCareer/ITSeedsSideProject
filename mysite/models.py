from django.db import models

# Create your models here.

class Test(models.Model):
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.account

class Account(models.Model):
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    passwordConfirmation = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=10, null=False)
    education = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.account