from django.urls import path
from . import views

urlpatterns = [
path('currents/', views.current, name ="currents"),
]