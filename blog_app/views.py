from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from blog_app.models import Blog, RelatedBlogProducts


def blog(request):
    blog_post = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blog_post})


# def blog_details(request, slug):
#     blogs = Blog.objects.get(slug=slug)
#     blog_products = RelatedBlogProducts.objects.filter(blog_product=slug)
#     return render(request, 'blog-detail.html', {'blogs': blogs, 'blog_product': blog_products})

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog-detail.html'
    context_object_name = 'blogs'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form_comment'] = RelatedBlogProducts.objects.filter(blog_product=kwargs['slug'])
    #     return context
