from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_client/', views.add_client, name='add_client'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_invoice/', views.add_invoice, name='add_invoice'),
    path('success/', views.success, name='success')
]