from django.shortcuts import render
from .models import Product#, Suply
from django.core.paginator import Paginator
# Create your views here.

def product(request):
    Products = Product.objects.all()
    paginator = Paginator(Products, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/products.html', context={'Products': page_obj})

def addproduct(request):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        product_id = request.POST.get('product_id', "")
        price = request.POST.get('price', "")
        quantity = request.POST.get('quantity', "")
        product = Product(product_id=product_id, name=name, price=price,quantity=quantity)
        product.save()
    return render(request, "product/addproduct.html",)
