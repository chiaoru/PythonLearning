"""
URL configuration for lcc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from news.views import news
from about.views import abouts
from product.views import product
from contact.views import contact

from member.views import register, login, logout, ChangePassword, updatePersonal

from cart.views import cart, addtocart, cartorder, cartok, cartordercheck, myorder, reportBank, ECPayCredit, bankfive

# 新增照片
from django.conf import settings
from django.conf.urls.static import static

from photos.views import uploadFile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', news),
    path('aboutme/', abouts),
    path('product/', product),
    path('contact/', contact),
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('', news),
    path('addtocart/<str:ctype>/<int:productid>/', addtocart),
    path('addtocart/<str:ctype>/', addtocart),
    path('cart/', cart),
    path('cartorder/', cartorder),
    path('cartok/', cartok),
    path('cartordercheck/', cartordercheck),
    path('myorder/', myorder),
    path('reportBank/', reportBank),
    path('creditcard/', ECPayCredit),
    path('bankfive/', bankfive),
    path('membercenter/', ChangePassword),
    path('photos/', uploadFile),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
