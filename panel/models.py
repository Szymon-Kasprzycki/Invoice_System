import datetime
from django.core.validators import MinValueValidator
from django.db import models
from decimal import Decimal

# Create your models here.
class Client(models.Model):
    class Meta:
        managed = True

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    nip = models.CharField(max_length=20)

    @property
    def full_name(self):
        """Returns the person's full name.

        Returns
        -------
        str
            string containing person's full name
        """
        return f'{self.first_name} {self.last_name}'

    @property
    def full_address(self):
        """Get full address of client

        Returns
        -------
        str
            string containing full address of client
        """
        return f'{self.address}, {self.postcode} {self.city}, {self.country}'

    def __str__(self):
        return self.full_name


class Product(models.Model):
    class Meta:
        managed = True

    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products_imgs/')

    def __str__(self):
        return self.name


class Invoice(models.Model):
    class Meta:
        managed = True

    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    invoice_date = models.DateField(auto_now_add=True)
    sell_date = models.DateField()
    invoice_number = models.CharField(max_length=255, default=f'FV/{datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}')
    seller = models.CharField(max_length=255, default='Magazine')
    total_net = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_brutto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_method = models.CharField(max_length=255, default="Web transfer")
    payment_date = models.DateField()

    def __str__(self):
        return self.invoice_number


class InvoicePosition(models.Model):
    class Meta:
        managed = True

    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=6, decimal_places=0, default=1, validators=[MinValueValidator(Decimal('1'))])
    total_net = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self):
        return f'{self.product}, {self.amount} {"pc" if self.amount == 1 else "pcs"}'
