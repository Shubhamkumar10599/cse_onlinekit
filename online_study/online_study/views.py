from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render


def index(requests):
    params = {'name': 'harry', 'place': 'mars'}
    return render(requests, 'index.html', params)


def loginPage(requests):
    return render(requests,'loginPage.html',{})

def JavascriptIntro(requests):
    return render(requests,'JavaScriptIntro.html',{})

def JavascriptHome(requests):
    return render(requests,'JavascriptHome.html',{})

def Home(requests):
    return render(requests,'index.html',{})






print('saurav')
print('shubham vs saurav')