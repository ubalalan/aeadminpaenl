from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('order/', views.order, name ="order"),
path('addorder/',views.addorder, name="addorder"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)