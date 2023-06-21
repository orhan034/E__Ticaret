from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Profil'''
    list_display = ('title','slug','id')


@admin.register(Gander)
class GanderAdmin(admin.ModelAdmin):
    '''Admin View for Profil'''
    list_display = ('title','slug','id')

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    '''Admin View for Profil'''
    list_display = ('title','slug','id')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Profil'''
    list_display = ('title','user','category',
                    'brand','ganders','slug','id')

@admin.register(ProductStok)
class ProductStokAdmin(admin.ModelAdmin):
    '''Admin View for Profil'''
    list_display = ('product','id')

@admin.register(ProductImg)
class ProductImgAdmin(admin.ModelAdmin):
    '''Admin View for Profil'''
    list_display = ('product','id')

@admin.register(ShopBasket)
class ShopBasketAdmin(admin.ModelAdmin):
    '''Admin View for Profil'''
    list_display = ('user','productss','price_all','count','date_now','id')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for Profil'''
    list_display = ('name','email','title','id')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for Profil'''
    list_display = ('user','product','star','title','id')
