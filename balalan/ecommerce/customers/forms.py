from dashboard.models import Product
from django import forms
from django.forms import ModelForm
from django.core.validators import FileExtensionValidator


class CustomerForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('name','address','city','state','zipcode','phone','email')
		

class ImportForm(forms.Form):
    import_file = forms.FileField(allow_empty_file=False, validators=[
                                  FileExtensionValidator(allowed_extensions=['csv', 'xls', 'xlsx'])], label="")
