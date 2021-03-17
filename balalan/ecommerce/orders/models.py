from django.db import models
import customers.models
import products.models
from datetime import datetime
from django.utils.safestring import mark_safe
# Create your models here.


order_status = (
    ("Gümrük İşlemleri", "Gümrük İşlemleri"),
    ("Yolda", "Yolda"),
    ("Teslim Edildi", "Teslim Edildi"),
)


class Order(models.Model):
    order_no = models.CharField(
        max_length=100, null=True, verbose_name="Sipariş Numarası")
    customer = models.ForeignKey(customers.models.Customer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Müşteri Bilgisi")
    product = models.ForeignKey(products.models.Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ürün Bilgisi")
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Fiyat") 
    quantity = models.IntegerField(
        default=0, null=True, blank=True, verbose_name="Adet")    
    date_added = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Oluşturulma Tarihi")
    complete = models.BooleanField(
        default=False,choices=order_status, verbose_name="Sipariş Durumu")
   
    def __str__(self):
        return str(self.customer) 
           
    @property
    def total(self):
        return(self.price * self.quantity)   


