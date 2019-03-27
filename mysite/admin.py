from django.contrib import admin
from .models import Test, Account, User

# Register your models here.
class PostTest(admin.ModelAdmin):
    list_display = ('account', 'password')

class AccountTest(admin.ModelAdmin):
    list_display = ('account', 'password', 'passwordConfirmation', 'email')

admin.site.register(Test, PostTest)
admin.site.register(Account, AccountTest)
admin.site.register(User)
