from django.shortcuts import render

from blog_app.models import Blog
from product_app.models import Products


def index(request):
    blog_post = Blog.objects.all()
    product = Products.objects.all()
    return render(request, 'index.html', {'blogs': blog_post, 'product': product})


def about(request):
    return render(request, 'about.html')
