from django.db import models


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
        "Returns the person's full name."
        return f'{self.first_name} {self.last_name}'


class Invoice(models.Model):
    class Meta:
        managed = True

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_date = models.DateField(auto_now_add=True)
    sell_date = models.DateField(auto_now_add=True)
    invoice_number = models.CharField(max_length=255)
    seller = models.CharField(max_length=255, default='Magazine')
    total_netto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_brutto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_method = models.CharField(max_length=255, default="Web transfer")
    payment_date = models.DateField(auto_now_add=True)


class Product(models.Model):
    class Meta:
        managed = True

    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products_imgs/')

    def __str__(self):
        return self.name
