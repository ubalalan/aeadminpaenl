
from django.db import models
#import source.models
#import products.models
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ürün Adı")
    product_id = models.CharField(max_length=200, verbose_name="Ürün ID")
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Fiyat")
    quantity = models.CharField(max_length=200, verbose_name="Stok Adet")

    def __str__(self):
        return self.product_id

class Logistics(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL, null=True, blank=True,verbose_name="Ürün Adı")
    domestic_shipping_price=models.DecimalField(max_digits=7, decimal_places=2, verbose_name="PTS Teslim Fiyatı")
    logistic_shipping_price=models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Lojistik Fiyatı")
    
    def __str__(self):
        return self.domestic_shipping_price
class Tax(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL, null=True, blank=True,verbose_name="Ürün Adı")
    customs_tax=models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Gümrük Ücreti")
    kdv=models.DecimalField(max_digits=7, decimal_places=2, verbose_name="KDV")
    
    def __str__(self):
        return self.domestic_shipping_price        

"""
class Suply(models.Model):
    aeproduct_id = models.ManyToManyField(Product,  null=True, verbose_name="AE- Ürün ID")
    name = models.ManyToManyField(Product, null=True,
                             blank=True,  verbose_name="Ürün Adı")
    price = models.ManyToManyField(Product.price, null=True,
                              blank=True, verbose_name="Ürün Fiyatı")
    sku = models.ManyToManyField(source.models.Source.product_sku, null=True,
                            blank=True, verbose_name="Pazaryeri SKU")
    pprice = models.ManyToManyField(source.models.Source.price, null=True, blank=True,
                               verbose_name="Pazaryeri Ürün Fiyatı")
    def __str__(self):
        return self.name
"""