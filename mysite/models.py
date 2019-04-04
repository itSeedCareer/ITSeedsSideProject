# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    account = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=45)
    password_confirmation = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    age = models.IntegerField()
    gender = models.CharField(max_length=45)
    education = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Account'


class User(models.Model):
    name = models.CharField(primary_key=True, max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'User'
