from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Vendor(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Admin")
    name = models.CharField(max_length=200, null=True,
                            verbose_name="Tedarikçi Adı")
    address = models.CharField(
        max_length=200, null=False, verbose_name="Adres")
    city = models.CharField(max_length=200, null=False, verbose_name="Şehir")
    state = models.CharField(max_length=200, null=False, verbose_name="Ülke")
    zipcode = models.CharField(
        max_length=200, null=False, verbose_name="Posta Kodu")
    phone = models.CharField(max_length=200, null=False, verbose_name="Telefon Numarası")
    date_added = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Oluşturulma Tarihi")
    email = models.CharField(max_length=200,default="test@mail.com", verbose_name="Mail")

    def __str__(self):
        return self.name
