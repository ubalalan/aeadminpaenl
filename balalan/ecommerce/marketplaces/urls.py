from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('marketplaces/', views.marketplace, name ="marketplaces"),
path('update/', views.update_prices, name='update-prices'),
path('delete/<pk>/', views.LinkDeleteView.as_view(), name="delete"),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)