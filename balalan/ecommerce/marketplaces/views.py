from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Marketplaces
from .forms import AddLinkForm
from django.views.generic import DeleteView
# Create your views here.
def marketplace(request):
    no_discounted = 0
    error = None

    form = AddLinkForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Ups ... couldn't get the name or the price"
        except:
            error = "Ups ... something went wrong"

    form = AddLinkForm()

    qs = Marketplaces.objects.all()
    items_no = qs.count()

    if items_no > 0:
        discount_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
            no_discounted = len(discount_list)

    context = {
        'qs': qs,
        'items_no': items_no,
        'no_discounted': no_discounted,
        'form': form,
        'error': error,
    }

    return render(request, 'marketplaces/marketplaces.html', context)

class LinkDeleteView(DeleteView):
    model = Marketplaces
    template_name = 'marketplaces/delete.html'
    success_url = reverse_lazy('marketplaces')

def update_prices(request):
    qs = Marketplaces.objects.all()
    for link in qs:
        link.save()
    return redirect('marketplaces')