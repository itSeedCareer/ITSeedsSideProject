from django.db import models

# Create your models here.

class Account(models.Model):
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.account