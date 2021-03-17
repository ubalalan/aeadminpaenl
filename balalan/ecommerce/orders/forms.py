from dashboard.models import Order, Customer
from django import forms
from django.forms import ModelForm
from django.core.validators import FileExtensionValidator


class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('order_no','price','quantity')
		model = Customer
		fields = ('name','address','city','state','zipcode','phone','email')
       
		
class ImportForm(forms.Form):
    import_file = forms.FileField(allow_empty_file=False, validators=[
                                  FileExtensionValidator(allowed_extensions=['csv', 'xls', 'xlsx'])], label="")
