from django.shortcuts import render
from django.http import HttpResponse
from .models import Client


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def add_client(request):
    return render(request, '../templates/add_client.html')


def register_client(request):
    try:
        new_client = Client()
        new_client.first_name = request.POST['first_name']
        new_client.last_name = request.POST['last_name']
        new_client.email = request.POST['email']
        new_client.phone = request.POST['phone']
        new_client.address = request.POST['address']
        new_client.city = request.POST['city']
        new_client.country = request.POST['country']
        new_client.postcode = request.POST['post-code']
        new_client.nip = request.POST['nip']
        new_client.save()
    except KeyError as e:
        return render(request, 'alert.html', context={'message': e})

    return HttpResponse("Client successfully saved!")
