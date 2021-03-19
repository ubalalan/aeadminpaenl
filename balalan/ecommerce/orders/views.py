from django.shortcuts import render
from .models import Order, Customer
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
  
def addordertest(request):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")
        phone=request.POST.get('phone',"")
        email=request.POST.get('email',"")
        customer = Customer(name=name,address=address,city=city,state=state,zipcode=zipcode,phone=phone,email=email)
        customer.save()
    
    if request.method == 'POST':
        order_no = request.POST.get('order_no', "")
        price = request.POST.get('price', "")
        quantity = request.POST.get('quantity', "")
        order = Order(order_no=order_no,price=price,quantity=quantity)
        order.save()
    return render(request, "order/addordertest.html",)
def testorder(request):
    Orders = Order.objects.all()
    paginator = Paginator(Orders, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'order/testorder.html', context={'Orders': page_obj})