from django.db import models


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    nip = models.CharField(max_length=255)


class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_date = models.DateField(auto_now_add=True)
    sell_date = models.DateField(auto_now_add=True)
    invoice_number = models.CharField(max_length=255)
    seller = models.CharField(max_length=255)
    total_netto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_brutto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_method = models.CharField(max_length=255)
    payment_date = models.DateField(auto_now_add=True)
