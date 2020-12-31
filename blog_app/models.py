import time
from datetime import datetime

from django.db import models

# Create your models here.
from django.utils.text import slugify

"""Creating Models for Blog and RelatedBlogProducts"""


class Blog(models.Model):
    """Blog image title description and min description slug for url date when is created and
    resources from when is taken the information.
    Function that adding data to slug the title then time example: "title"-20201230103428"""
    post_image = models.ImageField(upload_to='post_image')
    title = models.CharField(max_length=30)
    desc_min = models.TextField()
    description = models.TextField()
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)
    resources = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(self.title) + '-' + time.strftime("%Y%m%d%H%M%S")
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class RelatedBlogProducts(models.Model):
    """Model RelatedBlogProducts that will show kind of products that is Related with The blog that have relationship
    with it one to many one blog can have many products, products have  affiliate link to amazon """
    image_blog_product = models.ImageField(upload_to='image_blog_products')
    brand_blog_product = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    link_product_amazon = models.URLField()
    blog_rel = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_rel')
