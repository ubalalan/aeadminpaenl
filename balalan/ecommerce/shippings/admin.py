from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Shipping)
class ShippingAdmin(ImportExportModelAdmin):
    list_display = (
        'tracking_number',
        'agency_number',
        'customer',
        'weight',
        'shipping_status',
        'date_added'
    )

