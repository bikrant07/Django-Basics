from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm 

# Create your views here.
def contact(request):
    if request.method=="POST":
        form=NameForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            email=form.cleaned_data["email"]
            print(f"Name: {name}, Email: {email}")
            return HttpResponse("Thank you for submitting your name and email!")
    else:
        form=NameForm()
        return render(request,'contact.html',{"form":form})