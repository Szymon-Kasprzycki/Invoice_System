from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'homepage.html')


def success(request):
    return render(request, 'success.html')


def add_client(request):
    """
    Add client from request to the database

    :param request: The full HTTP request object for the current request (ex: an HTTP GET or POST)
    :return: It is a function that returns a view.
    """
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            if Client.objects.filter(email=request.POST['email']).exists():
                return render(request, 'alert.html',
                              context={'message': 'Declared email address already exists in database'})
            elif Client.objects.filter(phone=request.POST['phone']).exists():
                return render(request, 'alert.html',
                              context={'message': 'Declared phone number already exists in database'})
            elif Client.objects.filter(nip=request.POST['nip']).exists():
                return render(request, 'alert.html', context={'message': 'NIP number already exists in database'})
            else:
                form.save()
                return redirect('success')
        # TODO If not valid, add alert and render again
    else:
        form = ClientForm()
        return render(request, 'add_client.html', {'form': form})


def add_product(request):
    """
    If the request method is POST, validate the form, and if it's valid, add product to the database.
    If it's not valid, render the form again with an alert. If the request method is not POST, render the form again.

    :param request: The full HTTP request object for the current request (exactly as if you had accessed it in a view)
    :return: The form is being returned.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            if Product.objects.filter(name__iexact=request.POST['name']).exists():
                return render(request, 'alert.html',
                              context={'message': 'Declared product name already exists in database'})
            else:
                form.save()
                return redirect('success')
        # TODO If not valid, add alert and render again
    else:
        form = ProductForm()
        return render(request, 'add_product.html', {'form': form})


def add_invoice(request):
    if request.method == 'POST':
        print('1')
        form = InvoiceForm(request.POST)
        print(form.products)
        if form.is_valid():
            print('2')
            if Invoice.objects.filter(invoice_number__iexact=request.POST['invoice_number']).exists():
                return render(request, 'alert.html',
                              context={'message': 'That invoice already exists in database!'})
            else:
                form.save()
                return redirect('success')
        else:
            return render(request, 'alert.html',
                          context={'message': 'Form is not valid!'})
    else:
        print('3')
        form = InvoiceForm
        return render(request, 'add_invoice.html', {'form': form})
