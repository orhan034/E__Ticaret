from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator
from appUser.views import *
# Create your views here.

def sepetSay(request):
    if request.user.is_authenticated:
        return ShopBasket.objects.filter(user = request.user)
    else:
        return None

def index(request):
    products = ProductStok.objects.all().order_by('?')[:8]
    products_yeni = ProductStok.objects.all().order_by()[:8]
    context = {
        "title":"Anasayfa",
        'products':products,
        'products_yeni':products_yeni,
        "shopbasket": sepetSay(request)
    }
    return render(request, 'index.html',context)

def hakkimizda(request):
    context = {
        "title":"Hakkımızda",
        "shopbasket": sepetSay(request)
    }
    return render(request, 'hakkimizda.html',context)

def urunler(request):
    products = ProductStok.objects.all()
    gander = Gander.objects.all()
    categorys = Category.objects.all()

    paginator = Paginator(products, 7) 
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        "title":"Ürünler",
        'products':products,
        'gander':gander,
        'categorys':categorys,
        "shopbasket": sepetSay(request)
    }
    return render(request, 'urunler.html',context)
def gander(request,gen):
    products = ProductStok.objects.all()
    categorys = Category.objects.all()
    gander = Gander.objects.get(slug =  gen)
    gander = Gander.objects.all()
    genurun = ProductStok.objects.filter(product__ganders__slug = gen)
    product = get_object_or_404(Gander, slug = gen)

    paginator = Paginator(genurun, 7) 
    page_number = request.GET.get('page')
    genurun = paginator.get_page(page_number)
    
    context = {
        "title":"Ürünler",
        'product':product,
        'categorys':categorys,
        'gander':gander,
        'gander':gander,
        'genurun':genurun,
        'products':products,
        "shopbasket": sepetSay(request)
    }
    return render(request, 'gander.html', context)

def Kategori(request,category):
    gander = Gander.objects.all()
    products = ProductStok.objects.all()
    categorys = Category.objects.all()
    categor = Category.objects.get(slug =  category)
    categoryurun = ProductStok.objects.filter(product__category__slug = category)
    product = get_object_or_404(Category, slug = category)

    paginator = Paginator(categoryurun, 7) 
    page_number = request.GET.get('page')
    categoryurun = paginator.get_page(page_number)

    context = {
       "title":"Ürünler", 
       'products':products,
       'categorys':categorys,
       'categor':categor,
       'categoryurun':categoryurun,
       'product':product,
       'gander':gander,
       "shopbasket": sepetSay(request)
    }
    return render(request, 'category.html', context)
def detail(request, slug):
    prdct = Product.objects.get(slug=slug)
    comments = Comment.objects.filter(product = prdct)
    products = ProductStok.objects.all().order_by('?')[:4]
    product = get_object_or_404(ProductStok, product__slug = slug)
    puan = 0
    if request.method == 'POST':
        # Sepet start
        if request.POST.get('shopbutton')=='sepet':
            size = request.POST.get('size')
            count = int(request.POST.get('count'))

            if product.product.category.slug == 'kiyafet':
                try:
                    prod = ProductStok.objects.filter(product__size__title=size, 
                                                    product__slug = slug).get()
                    price_all = prod.product.price * count
             

                    shopprod = ShopBasket.objects.filter(user = request.user, productss = prod)
                    if shopprod.exists():
                        shopprod = shopprod.get()
                        shopprod.count += count
                        shopprod.price_all += price_all
                        shopprod.save()
                    else:
                        shopb = ShopBasket(user = request.user, productss = prod, count = count, price_all=price_all)
                        print(shopb.productss.product.size)
                        shopb.save()
                except:
                    messages.warning(request, 'Aradığın beden mağazada bulunmamaktadır!')
                
            if product.product.category.slug == 'ayakkabi':
                try:
                    prod = ProductStok.objects.filter(product__size__title=size, 
                                                    product__slug = slug).get()
                    print('PROD================',prod)
                    price_all = prod.product.price * count
             

                    shopprod = ShopBasket.objects.filter(user = request.user, productss = prod)
                    if shopprod.exists():
                        shopprod = shopprod.get()
                        shopprod.count += count
                        shopprod.price_all += price_all
                        shopprod.save()
                    else:
                        shopb = ShopBasket(user = request.user, productss = prod, count = count, price_all=price_all)
                        print(shopb.productss.product.size)
                        shopb.save()
                except:
                    messages.warning(request, 'Aradığın beden mağazada bulunmamaktadır!')
                
            if product.product.category.slug == 'aksesuar' or product.product.category.slug == 'elektronik':
                try:
                    prod = ProductStok.objects.filter(product__slug = slug).get()
                    print('PROD================',prod)
                    price_all = prod.product.price * count
                

                    shopprod = ShopBasket.objects.filter(user = request.user, productss = prod)
                    if shopprod.exists():
                        shopprod = shopprod.get()
                        shopprod.count += count
                        shopprod.price_all += price_all
                        shopprod.save()
                    else:
                        shopb = ShopBasket(user = request.user, productss = prod, count = count, price_all=price_all)
                        shopb.save()
                except:
                    messages.warning(request, 'Aradığın beden mağazada bulunmamaktadır!')
                return redirect('/detay/'+ slug+'/')
        # Sepet end
        
        elif request.POST.get('submit')=="comment":
            title = request.POST.get('title')
            text = request.POST.get('text')
            try:
                star = int(request.POST.get('star'))
            except:
                return redirect('/detay/'+ slug+'/')
           
            comment = Comment(title=title, text=text, 
                              star=star, user=request.user, product=prdct)
            comment.save()
          
            for i in comments:
                puan += i.star 
            prdct.stars = round(puan/len(comments))
            prdct.save()


            return redirect('/detay/'+ slug+'/')
            
            
    context = {
        'product':product,
        'products':products,
        'comments':comments,
        "shopbasket": sepetSay(request)
    }
    return render(request, 'detail.html', context)
    
def kart(request):
    shopbasket = ShopBasket.objects.filter(user = request.user)

    toplam = 0
    for i in shopbasket:
        toplam +=i.price_all

    if request.method =='POST':
        for k,v in dict(request.POST).items():
            if k != "csrfmiddlewaretoken":
                try:
                    v[0] = int(v[0])
                except:
                    return redirect('kart')
                
                shopb = shopbasket.get(id=k[5:])
                if v[0] == '0':
                    shopb.delete()
                elif v[0] > 0:
                    shopb.count = int(v[0])
                    shopb.price_all = shopb.productss.product.price * int(v[0])
                    shopb.save()
                else:
                    return redirect('kart')
        return redirect('kart')


    context = {
        "title":"Sepet",
        'shopbasket':shopbasket,
        'toplam':toplam,
        
    }
    return render(request, 'kart.html', context)

def ShopBasketDelete(request,id):
    shopbasket = ShopBasket.objects.get(id = id)
    shopbasket.delete()
    return redirect('kart')


def iletisim(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('gonder') == 'Kaydet':
            name = request.POST.get('name')
            email = request.POST.get('email')
            title = request.POST.get('title')
            text = request.POST.get('text')

            contact = Contact(name=name,email=email,title=title,text=text)
            contact.save()
            return redirect('iletisim')
    context = {
        "title":"İletişim",
        "shopbasket": sepetSay(request)
    }
    return render(request, 'iletisim.html', context)
