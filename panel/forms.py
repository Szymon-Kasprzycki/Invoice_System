from django import forms
from .models import *


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, product):
        return f'{product.name}'


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
                  'payment_date', 'products']
        # widgets = {
        #     'sell_date': DateInput(),
        #     'payment_date': DateInput(),
        #     'products': forms.ModelMultipleChoiceField(
        #         queryset=Product.objects.all(),
        #         widget=forms.CheckboxSelectMultiple()
        #     )
        # }
        sell_date = forms.DateInput()
        payment_date = forms.DateInput()
        products = CustomMMCF(
            queryset=Product.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            to_field_name='products'
        )