from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def findSquare(request,num):
    return HttpResponse(num*num)

def greetUser(request,name):
    return HttpResponse(f"Hello {name},welcome to out site!")
    