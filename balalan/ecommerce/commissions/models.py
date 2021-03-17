#from .models import Product
from django.db import models
import products.models 
import tracks.models
from decimal import Decimal
# Create your models here.

class Commission(models.Model):
    ae_product = models.ForeignKey(products.models.Product, on_delete=models.SET_NULL, null=True, blank=True,verbose_name="Ürün Bilgisi")
    track_product = models.ForeignKey(tracks.models.Track, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tedarik")
    dollar = models.DecimalField(
        max_digits=3, decimal_places=2, verbose_name="Kur Fiyatı")
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Ağırlık")
    y_cargo = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Yurtiçi Kargo")
    logistics = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Lojistik")
    customs = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Gümrük Vergisi")
    tax = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="KDV")
    p_cost = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Ürün Maliyeti")
    coupon = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Kuponlar")
    ae_commission_rate = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Platform Komisyon Oranı")
    affiliate_rate = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Affiliate")    
  
    def __str__(self):
       return str(self.ae_product)

    @property
    def m_price(self):
        y= Decimal(self.track_product.price / self.dollar)
        return round(y,2)

    @property
    def p_cost(self):
        x=Decimal(self.m_price + self.y_cargo + self.logistics)
        return round(x,2)
   
    @property
    def ae_commission(self):
        ae=Decimal(self.ae_commission_rate * self.ae_product.price) 
        return round(ae,2)
    
    @property
    def affiliate(self):
        af=Decimal(self.affiliate_rate * self.ae_product.price) 
        return round(af,2)


    @property
    def sum_commissions(self):
        c=Decimal(self.coupon + self.ae_commission + self.affiliate)
        return round(c,2)
    @property
    def ae_remaining(self):
        return(self.ae_product.price - self.sum_commissions)
    @property
    def net_profit(self):
        return(self.ae_remaining-self.p_cost) 
    @property
    def net_profit_tl(self):
        l=Decimal(self.net_profit * self.dollar)  
        return round(l,2)
    
    @property
    def profit_margin(self):
        z=Decimal(self.net_profit / self.p_cost)
        return round(z,2)