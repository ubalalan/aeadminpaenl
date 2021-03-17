from django.shortcuts import render
from .models import Order
from django.core.paginator import Paginator
# Create your views here.

def order(request):
    Orders = Order.objects.all()
    paginator = Paginator(Orders, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'order/orders.html', context={'Orders': page_obj})

def addorder(request):
    if request.method == 'POST':
        order_no = request.POST.get('order_no', "")
        price = request.POST.get('price', "")
        quantity = request.POST.get('quantity', "")
        order = Order(order_no=order_no,price=price,quantity=quantity)
        order.save()
    return render(request, "order/addorder.html",)
  
  
