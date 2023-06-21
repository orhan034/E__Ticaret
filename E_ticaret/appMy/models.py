from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from appUser.models import *
# Create your models here.

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    slug = models.SlugField(("Slug Kategori"), blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title

class Gander(models.Model):
    title = models.CharField(("Cinsiyet"), max_length=50)
    slug = models.SlugField(("Slug Renk"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Gander, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Size(models.Model):
    title = models.CharField(("Beden"), max_length=50)
    slug = models.SlugField(("Slug Beden"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Size, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Product(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    title = models.CharField(("Başlık"), max_length=50)
    brand = models.CharField(("Marka"), max_length=50)
    text = models.TextField(("Açıklama"), max_length=1000)
    detail = models.TextField(("Özellikler"), max_length=800)
    price = models.FloatField(("Fiyat"),null=True)
    stars = models.FloatField(("Puan"), default=0)
    size = models.ManyToManyField(Size, verbose_name=("Ürün beden"), blank=True)
    ganders = models.ForeignKey(Gander, verbose_name=("Cinsiyet"), on_delete=models.CASCADE,null=True, blank=True)
    date_now = models.DateTimeField(("Ürün giriş tarihi"), auto_now_add=True, null=True)
    image = models.ImageField(("Resim"), upload_to="product", null=True)
    stok = models.IntegerField(("Stok"), null=True)
    slug = models.SlugField(("Slug Title"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
class ProductImg(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE, null=True)
    image = models.ImageField(("Resim"), upload_to="product")
    
    def __str__(self):
        return self.product.title
    
class ProductStok(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE, null=True)
    # size = models.ForeignKey(Size, verbose_name=("Ürün Beden"), on_delete=models.CASCADE, null=True, blank=True)
    images = models.ManyToManyField(ProductImg, verbose_name=("Ürün Fotoğrafları"))

    def __str__(self):
        return self.product.title
    
class ShopBasket(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    productss = models.ForeignKey(ProductStok, verbose_name=("Ürün"), on_delete=models.CASCADE, null=True)
    price_all = models.FloatField(("Toplam fiyat"), default=0)
    count = models.IntegerField(("Adet"), default=0)
    date_now = models.DateField(("Sepet Tarihi"), auto_now_add=True, null=True)

    def __str__(self):
        return self.productss.product.title
    
class Contact(models.Model):
    name = models.CharField(("İsim"), max_length=50)
    email = models.CharField(("Email"), max_length=50)
    title = models.CharField(("Mesaj Başlığı"), max_length=50)
    text = models.TextField(("Mesaj"), max_length=1000)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.TextField(("Yurum"), max_length=1000)
    date_now = models.DateTimeField(("Tarih"), auto_now_add=True)
    star = models.IntegerField(("Yorum Puanı"), default=5)

    def __str__(self):
        return self.title


        