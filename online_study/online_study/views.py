from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render


def index(requests):
    params = {'name': 'harry', 'place': 'mars'}
    return render(requests, 'index.html', params)


def loginPage(requests):
    return render(requests,'loginPage.html',{})






print('saurav')
print('shubham vs saurav')