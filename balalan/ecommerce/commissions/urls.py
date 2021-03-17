from django.urls import path
from . import views

urlpatterns = [
path('commission/', views.commission, name ="commission"),
]