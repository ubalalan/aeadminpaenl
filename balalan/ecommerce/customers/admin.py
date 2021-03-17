from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


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
