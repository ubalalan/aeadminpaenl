from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('order/', views.order, name ="order"),
path('addorder/',views.addorder, name="addorder"),
path('addordertest/',views.addordertest, name="addordertest"),
path('testorder/',views.testorder, name="testorder"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)