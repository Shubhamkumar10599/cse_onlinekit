
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from . import views
from . import cview
from . import cppviews
from . import javaview
from . import htmlview
from . import pythonview
from . import djangoview
from . import gateview
from . import cssview
from . import sqlview
from . import exerciseview
from . import quizview



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
    url(r'^jsArray/$', views.jsArray, name='jsArray'),




    url(r'^Cintro/$', cview.Cintro, name='Cintro'),
    url(r'^Cconst/$', cview.Cconst, name='Cconst'),
    url(r'^Cvar/$', cview.Cvar, name='Cvar'),
    url(r'^Ckey/$', cview.Ckey, name='Ckey'),





    url(r'^Cppintro/$', cppviews.Cppintro, name='Cppintro'),



    url(r'^Djangointro/$', djangoview.Djangointro, name='Djangointro'),




    url(r'^Javaintro/$', javaview.Javaintro, name='Javaintro'),





    url(r'^HTMLintro/$', htmlview.HTMLintro, name='HTMLintro'),





    url(r'^Pythonintro/$', pythonview.Pythonintro, name='Pythonintro'),



    url(r'^Cssintro/$', cssview.Cssintro, name='Cssintro'),



    url(r'^Gatesyl/$', gateview.Gatesyl, name='Gatesyl'),






    url(r'^Sqlintro/$', sqlview.Sqlintro, name='Sqlintro'),



    url(r'^Quiz/$', quizview.Quiz, name='Quiz'),





    url(r'^Exercise/$', exerciseview.Exercise, name='Exercise'),


]
