from django.shortcuts import render

def one(request):
    return render(request,'one.html')

def two(request):
    return render(request,'two.html')

def three(request):
    return render(request,'three.html')

def four(request):
    return render(request,'four.html')    