from django.db import models

# Create your models here.


class Source(models.Model):

    product_sku = models.CharField(max_length=200, verbose_name="Ürün ID")
    name = models.CharField(max_length=200, verbose_name="Ürün Adı")
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Orjinal Fiyat")
    discount_price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="İndirimli Fiyat")
    quantity = models.CharField(max_length=200, verbose_name="Stok Adet")
    link = models.CharField(max_length=200, null=True,verbose_name="Ürün Linki")
    marketplace = models.CharField(max_length=200, null=True,verbose_name="Pazaryeri") 

    def __str__(self):
        return self.name