from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product

# Create your views here.

def product_list(request):
    # 1. Get all products with price > 10000.
    # products=Product.objects.filter(price__gt=10000)
    
    # 2. Search products containing "phone".
    # products=Product.objects.filter(name__icontains="phone")
    
    # 3. Sort products by highest price.
    # products=Product.objects.order_by("-price")
    
    # 4. Count total products.
    products=Product.objects.count()
    
    context={
        "products": products
    }
    return render(request,"products.html",context)