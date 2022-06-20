from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_client/', views.add_client, name='add_client'),
    path('register_client/', views.register_client, name='register_client'),
]