from django.shortcuts import render
from .models import Customer 
from django.core.paginator import Paginator

# Create your views here.

def customer(request):
    Customers = Customer.objects.all()
    paginator = Paginator(Customers, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'customer/customers.html', context={'Customers': page_obj})
