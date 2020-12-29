from django.db import models


# Create your models here.
class Products(models.Model):
    image_product = models.ImageField(upload_to='image_products')
    brand_product = models.CharField(max_length=50)
    about_product = models.TextField()
    colour = models.CharField(max_length=30)
    model_name = models.CharField(max_length=100)
    more_details = models.TextField()
    category = models.CharField(max_length=50)
    link_product_amazon = models.URLField()
    date = models.DateTimeField(auto_now_add=True)
