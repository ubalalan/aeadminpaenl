from django.db import models
from datetime import datetime

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True,
                            verbose_name="Müşteri Adı")
    address = models.CharField(
        max_length=200, null=False, verbose_name="Adres")
    city = models.CharField(max_length=200, null=False, verbose_name="Şehir")
    state = models.CharField(max_length=200, null=False, verbose_name="Ülke")
    zipcode = models.CharField(
        max_length=200, null=False, verbose_name="Posta Kodu")
    phone = models.CharField(max_length=200, null=False,
                             verbose_name="Telefon Numarası")
    date_added = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Oluşturulma Tarihi")
    email = models.CharField(
        max_length=200, default="test@mail.com", verbose_name="Mail")

    def __str__(self):
        return self.name


order_status = (
    ("Gümrük İşlemleri", "Gümrük İşlemleri"),
    ("Yolda", "Yolda"),
    ("Teslim Edildi", "Teslim Edildi"),
)


class Order(models.Model):
    order_no = models.CharField(
        max_length=100, null=True, verbose_name="Sipariş Numarası")
    product = models.CharField(
        max_length=200, null=True, verbose_name="Ürün Adı")
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Fiyat")
    quantity = models.IntegerField(
        default=0, null=True, blank=True, verbose_name="Adet")
    date_added = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Oluşturulma Tarihi")
    complete = models.CharField(
        default=False, choices=order_status, max_length=20, verbose_name="Sipariş Durumu")

    def __str__(self):
        return str(self.product)

    @property
    def total(self):
        return(self.price * self.quantity)
