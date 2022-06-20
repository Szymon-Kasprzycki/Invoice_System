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
        if Client.objects.filter(email=request.POST['email']).exists():
            return render(request, '../templates/alert.html', context={'message': 'Email already exists in database'})
        elif Client.objects.filter(phone=request.POST['phone']).exists():
            return render(request, '../templates/alert.html', context={'message': 'Phone already exists in database'})
        elif Client.objects.filter(nip=request.POST['nip']).exists():
            return render(request, '../templates/alert.html', context={'message': 'NIP number already exists in database'})
        else:
            client = Client.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                phone=request.POST['phone'],
                address=request.POST['address'],
                city=request.POST['city'],
                postcode=request.POST['post-code'],
                country=request.POST['country'],
                nip=request.POST['nip']
            )
            client.save()
    except KeyError as e:
        return render(request, '../templates/alert.html', context={'message': e})

    return HttpResponse("Client successfully saved!")
