from django.contrib.auth import login
from django.urls import path

from mainapp.views import products, product

app_name = 'auth'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', login, name='login'),



]
