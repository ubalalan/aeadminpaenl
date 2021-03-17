from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = (
        'order_no',
        'customer',
        'product',
        'quantity',
        'price',
        'total',
        'complete',
        'date_added'
    )

    search_fields = ('name',)
