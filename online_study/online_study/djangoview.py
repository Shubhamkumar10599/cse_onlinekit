from django.shortcuts import render

def Djangointro(requests):
    return render(requests,'django files/Djangointro.html',{})