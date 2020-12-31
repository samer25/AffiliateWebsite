from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from blog_app.models import Blog

"""adding function view to display all blog and using class base view for blog details"""


def blog(request):
    """adding function view to display all blog that passing blog data to template blog.html """

    blog_post = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blog_post})


class BlogDetailView(DetailView):
    """using class base view for displaying blog details of specific blog that recognise with slug """
    model = Blog
    template_name = 'blog-detail.html'
    context_object_name = 'blogs'

