from .models import Product
from django import forms
from django.forms import ModelForm
from django.core.validators import FileExtensionValidator


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('name','product_id','price','quantity','image')
		
	

class ImportForm(forms.Form):
    import_file = forms.FileField(allow_empty_file=False, validators=[
                                  FileExtensionValidator(allowed_extensions=['csv', 'xls', 'xlsx'])], label="")
