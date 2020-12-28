from django.shortcuts import render

# Create your views here.
from product_app.models import Products


def products(request):
    product = Products.objects.all()
    return render(request, 'products.html', {'product': product})


def product_details(request, pk):
    product = Products.objects.get(pk=pk)
    return render(request, 'product_details.html', {'product': product})
