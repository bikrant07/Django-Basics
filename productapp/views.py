from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product

# Create your views here.

def product_list(request,id):
    product=get_object_or_404(Product,id=id)
    context={
        "product": product
    }
    return render(request,"products.html",context)