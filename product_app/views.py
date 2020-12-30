from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from product_app.models import Products


def products(request):
    product = Products.objects.all()
    return render(request, 'products.html', {'product': product})


# def product_details(request, pk):
#     product = Products.objects.get(pk=pk)
#     return render(request, 'product_details.html', {'product': product})


class ProductDetailView(DetailView):
    model = Products
    template_name = 'product_details.html'
    context_object_name = 'product'
