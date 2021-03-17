from django.shortcuts import render
from .models import Source
from django.core.paginator import Paginator
# Create your views here.

def source(request):
    Sources = Source.objects.all()
    paginator = Paginator(Sources, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'source/source.html', context={'Sources': page_obj})

def addsource(request):
    if request.method == 'POST':
        product_sku  = request.POST.get('product_sku', "")
        name = request.POST.get('name', "")
        price = request.POST.get('price', "")
        discount_price = request.POST.get('discount_price', "")
        quantity = request.POST.get('quantity', "")
        link = request.POST.get('link', "")
        marketplace = request.POST.get('marketplace', "")
        source = Source(product_sku=product_sku, name=name, price=price,discount_price=discount_price,quantity=quantity,link=link,marketplace=marketplace)
        source.save()
    return render(request, "source/addsource.html",)