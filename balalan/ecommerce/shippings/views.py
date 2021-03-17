from django.shortcuts import render
from .models import Shipping
from django.core.paginator import Paginator
# Create your views here.

def shipping(request):
    Shippings = Shipping.objects.all()
    paginator = Paginator(Shippings, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shipping/shipping.html', context={'Shippings': page_obj})