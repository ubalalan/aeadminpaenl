from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('source/', views.source, name ="source"),
path('addsource/',views.addsource, name="addsource"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)