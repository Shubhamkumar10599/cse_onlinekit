from django.shortcuts import render

def Exercise(requests):
    return render(requests,'Exercise files/Exercise.html',{})