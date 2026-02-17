from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def printName(request):
    if request.method=="POST":
        name = request.POST.get("name")
        context = {
            "name": name
        }
        return render(request,'printName.html',context)
    else:
        return render(request,'inputName.html')