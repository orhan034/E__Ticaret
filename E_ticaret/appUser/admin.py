from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    '''Admin View for Profil'''
    list_display = ('user','phone','id')