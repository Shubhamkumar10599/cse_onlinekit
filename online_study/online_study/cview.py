from django.shortcuts import render

def Cintro(requests):
    return render(requests,'c lamguageFiles/c introduction.html',{})

def Cconst(requests):
    return render(requests,'c lamguageFiles/c Constants.html',{})


def Cvar(requests):
    return render(requests,'c lamguageFiles/c Variables.html',{})


def Ckey(requests):
    return render(requests,'c lamguageFiles/c Keywords.html',{})