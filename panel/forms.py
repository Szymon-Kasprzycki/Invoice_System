from django import forms
from .models import *


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, product):
        return f'{product.name}'


class DateInput(forms.DateInput):
    class Meta:
        input_type = 'date'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'postcode', 'city', 'country', 'nip']
        widgets = {
            'email': forms.EmailInput(),
        }


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client', 'invoice_number', 'sell_date', 'seller', 'total_net', 'total_brutto', 'payment_method',
                  'payment_date']
        labels = {
            'client': 'Client',
            'invoice_number': 'Invoice number',
            'sell_date': 'Sell date',
            'seller': 'Seller',
            'total_net': 'Total net',
            'total_brutto': 'Total brutto',
            'payment_method': 'Payment method',
            'payment_date': 'Payment date'
        }
        widgets = {
            'sell_date': forms.DateInput(
                format='%Y/%m/%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            'payment_date': forms.DateInput(
                format='%Y/%m/%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }


PositionFormSet = forms.modelformset_factory(
    InvoicePosition,
    fields=['product', 'amount', 'total_net'],
    extra=1,
    widgets={
        'amount': forms.NumberInput(),
        'total_net': forms.NumberInput()
    }

)
