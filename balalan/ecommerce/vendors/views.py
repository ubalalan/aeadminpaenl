from django.shortcuts import render
from .models import Vendor
from django.core.paginator import Paginator
# Create your views here.

def vendor(request):
    Vendors = Vendor.objects.all()
    paginator = Paginator(Vendors, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'vendor/vendor.html', context={'Vendors': page_obj})
