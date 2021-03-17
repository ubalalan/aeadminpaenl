from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin):
    list_display = (
        'name',
        'address',
        'city',
        'state',
        'zipcode',
        'phone',
        'date_added',
        'email'

    )

