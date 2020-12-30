import time

from django.db import models


# Create your models here.
from django.utils.text import slugify


class Products(models.Model):
    image_product = models.ImageField(upload_to='image_products')
    brand_product = models.CharField(max_length=50)
    about_product = models.TextField()
    colour = models.CharField(max_length=30)
    model_name = models.CharField(max_length=100)
    more_details = models.TextField()
    category = models.CharField(max_length=50)
    link_product_amazon = models.URLField()
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(self.brand_product) + '-' + time.strftime("%Y%m%d%H%M%S")
        super(Products, self).save(*args, **kwargs)
