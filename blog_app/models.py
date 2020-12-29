from datetime import datetime

from django.db import models


# Create your models here.
class Blog(models.Model):
    post_image = models.ImageField(upload_to='post_image')
    title = models.CharField(max_length=30)
    description = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)
    resources = models.CharField(max_length=100)


class RelatedBlogProducts(models.Model):
    image_blog_product = models.ImageField(upload_to='image_blog_products')
    brand_blog_product = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    link_product_amazon = models.URLField()
    blog_product = models.ManyToManyField(Blog)
