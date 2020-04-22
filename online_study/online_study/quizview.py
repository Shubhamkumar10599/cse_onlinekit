from django.shortcuts import render

def Quiz(requests):
    return render(requests,'Quiz files/Quiz.html',{})