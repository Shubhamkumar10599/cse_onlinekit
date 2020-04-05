from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render


def index(requests):
    params = {'name': 'harry', 'place': 'mars'}
    return render(requests, 'index.html', params)


def loginPage(requests):
    return render(requests,'loginPage.html',{})

def JavascriptIntro(requests):
    return render(requests,'JavascriptFiles/JavaScriptIntro.html',{})

def javascriptVariables(requests):
    return render(requests,'JavascriptFiles/jsVariables.html',{})


def jsDatatypes(requests):
    return render(requests,'JavascriptFiles/jsDatatypes.html',{})

def jsTypeConversion(requests):
    return render(requests,'JavascriptFiles/jsTypeconversion.html',{})

def Home(requests):
    return render(requests,'index.html',{})






print('saurav')
print('shubham vs saurav')