from django.shortcuts import render

# Create your views here.
from blog_app.models import Blog, RelatedBlogProducts


def blog(request):
    blog_post = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blog_post})


def blog_details(request, pk):
    blogs = Blog.objects.get(pk=pk)
    blog_products = RelatedBlogProducts.objects.filter(blog_product=pk)
    return render(request, 'blog-detail.html', {'blogs': blogs, 'blog_product': blog_products})
