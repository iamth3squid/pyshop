from django.shortcuts import render
from django.http import HttpResponse
from . models import Product


# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'product': products})


def product_new(request):
    return HttpResponse('Welcome to the new products page')
