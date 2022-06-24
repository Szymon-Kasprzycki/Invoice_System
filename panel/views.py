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
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            if Product.objects.filter(name__iexact=request.POST['name']).exists():
                return render(request, 'alert.html',
                              context={'message': 'Declared phone number already exists in database'})
            else:
                form.save()
                return redirect('success')
        # TODO If not valid, add alert and render again
    else:
        form = ProductForm()
        return render(request, 'add_product.html', {'form': form})
