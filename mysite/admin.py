from django.contrib import admin
from .models import Account

# Register your models here.
class PostAccount(admin.ModelAdmin):
    list_display = ('account', 'password')

admin.site.register(Account, PostAccount)
