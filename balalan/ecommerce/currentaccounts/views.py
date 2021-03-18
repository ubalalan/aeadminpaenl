from django.shortcuts import render
# Create your views here.

def current(request):
    return render(request, 'currents/currents.html')