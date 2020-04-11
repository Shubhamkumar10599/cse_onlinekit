
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from . import views
from . import cview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url(r'^loginPage/$', views.loginPage, name='loginPage'),
    url(r'^JavascriptIntro/$', views.JavascriptIntro, name='JavascriptIntro'),
    url(r'^javascriptVariables/$', views.javascriptVariables, name='javascriptVariables'),
    url(r'^Home/$', views.Home, name='Home'),
    url(r'^jsDatatypes/$', views.jsDatatypes, name='jsDatatypes'),
    url(r'^jsTypeConversion/$', views.jsTypeConversion, name='jsTypeConversion'),
    url(r'^jsString/$', views.jsString, name='jsString'),



    url(r'^Cintro/$', cview.Cintro, name='Cintro'),


]
