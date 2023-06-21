"""eticaret URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from appMy.views import *
from appUser.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('hakkimizda/', hakkimizda, name="hakkimizda"),
    path('urunler/', urunler, name="urunler"),
    path('urun/<gen>/', gander, name="gander"),
    path('kategori/<category>/', Kategori, name="Kategori"),
    path('detay/<slug>/', detail, name="detail"),
    path('iletisim/', iletisim, name='iletisim'),
    path('kart/', kart, name='kart'),
    path('ShopBasketDelete/<id>/', ShopBasketDelete ,name='ShopBasketDelete'),
    # USER
    path('kayit/', kayit, name='kayit'),
    path('logout/', logoutUser, name = "logoutUser"),
    path('profil/', profilUser, name='profilUser'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
