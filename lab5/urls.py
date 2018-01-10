"""lab5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from my_app.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    url(r'^admin', admin.site.urls),
    url(r'', include('my_app.urls')),
    url(r'^orders', OrdersView.as_view(), name='orders_url'),
    url(r'^bd', bd, name='bd'),
    url(r'^tovar', TovarList.as_view(), name='tovar'),
    url(r'^shop1', ShopList1.as_view(), name='shop1'),
    url(r'^shop', ShopList.as_view(), name='shop'),
    url(r'^workers', WorkerList.as_view(), name='workers'),
    url(r'^main', main, name='main'),
    url(r'^login', login, name='login'),
    url(r'^success', success, name='success'),
    url(r'^registration2', registration2, name='registration2'),
    url(r'^registration', registration, name='registration'),
    url(r'^$', main, name='main'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
