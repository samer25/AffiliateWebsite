from django.shortcuts import render

from blog_app.models import Blog
from product_app.models import Products

"""creating functon view for display home and about pages"""


def index(request):
    """function view that passing Blog data and product data to display on home page latest blogs and products """
    blog_post = Blog.objects.all()
    product = Products.objects.all()
    return render(request, 'index.html', {'blogs': blog_post, 'product': product})


def about(request):
    """about function view to display about page"""
    return render(request, 'about.html')
