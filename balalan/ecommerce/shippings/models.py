from django.db import models
import customers.models 
from datetime import datetime
# Create your models here.

shipping_status = (
    ("Gümrük İşlemleri", "Gümrük İşlemleri"),
    ("Yolda", "Yolda"),
    ("Teslim Edildi", "Teslim Edildi"),
)

class Shipping(models.Model):
    tracking_number = models.CharField(
        max_length=100, null=True, verbose_name="Takip Numarası")
    agency_number = models.CharField(
        max_length=100, null=True, verbose_name="Acenta Numarası")
    customer = models.ForeignKey(customers.models.Customer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Müşteri")
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Ağırlık")
    to_country = models.CharField(
        max_length=100, null=True, verbose_name="Varış Ülkesi")
    shipping_status = models.CharField(
        max_length=50, choices=shipping_status, default=True, verbose_name="Sipariş Durumu:")
    date_added = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return str(self.tracking_number)


