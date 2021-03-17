from django.shortcuts import render
from .models import Commission
from django.core.paginator import Paginator

def commission(request):
    Commissions = Commission.objects.all()
    paginator = Paginator(Commissions, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'commission/commissions.html', context={'Commissions': page_obj})