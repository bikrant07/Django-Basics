from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category
from .forms import ProductForm

# Create your views here.

def product_list(request):
    # 1. Get all products with price > 10000.
    # products=Product.objects.filter(price__gt=10000)
    
    # 2. Search products containing "phone".
    # products=Product.objects.filter(name__icontains="phone")
    
    # 3. Sort products by highest price.
    # products=Product.objects.order_by("-price")
    
    # 4. ORM Queries.
    # products=Product.objects.filter(category__name="Food")
    
    category=Category.objects.get(name="Food")
    
    context={
        "products": category.products.all()
    }
    return render(request,"products.html",context)

def add_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            price=form.cleaned_data["price"]
            if price<=0:
                return HttpResponse("Price must be greater than zero.")
            form.save()
            return HttpResponse("Product added successfully!")
    else:
        form=ProductForm()
    return render(request,"form.html",{"form":form})
        