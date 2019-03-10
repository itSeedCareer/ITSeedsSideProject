from django.contrib import admin
from .models import Test

# Register your models here.
class PostTest(admin.ModelAdmin):
    list_display = ('account', 'password')

admin.site.register(Test, PostTest)
