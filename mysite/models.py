from django.db import models

# Create your models here.

# class Test(models.Model):
#     account = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.account

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

class User(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=False)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name