"""Lotek_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from Lotek import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^random$', views.random, name='random'),
    url(r'^ranking', views.ranking, name='ranking'),
    url(r'^user', views.user, name='user'),
    url(r'^money', views.money, name='money'),
    url(r'^admin/', admin.site.urls),
]
