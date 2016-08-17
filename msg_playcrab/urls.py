"""msg_playcrab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',include('urls.UcKeyurl',namespace='UcKey',app_name='Uckey'),name='login'),
    url(r'^DataCenter/', include('urls.DataCenterurl', namespace='DataCenter', app_name='DataCenter'), name='DataCenter'),
    url(r'^LogCenter/', include('urls.LogCenterurl', namespace='LogCenter', app_name='LogCenter'), name='LogCenter')
]




