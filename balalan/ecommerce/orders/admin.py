from django.contrib import admin
from .models import Order
from customers.models import Customer
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = (
        'order_no',
        'product',
        'quantity',
        'price',
        'total',
        'complete',
        'date_added'
    )

    search_fields = ('name',)


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = (
        'name',
        'address',
        'city',
        'state',
        'zipcode',
        'phone',
        'date_added'
    )

    search_fields = ('name',)
