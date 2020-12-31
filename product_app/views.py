from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from product_app.models import Products


def products(request):
    """crating function view to pass product data  to product.html"""
    product = Products.objects.all()
    return render(request, 'products.html', {'product': product})



class ProductDetailView(DetailView):
    """crating class base view to assess to Product details"""
    model = Products
    template_name = 'product_details.html'
    context_object_name = 'product'
