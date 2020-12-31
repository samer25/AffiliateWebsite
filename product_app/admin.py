from django.contrib import admin

# Register your models here.
from product_app.models import Products

"""Registering Products to admin panel"""


class ProductsAdmin(admin.ModelAdmin):
    """adding list display for admin page to display it and filters """
    list_display = ("brand_product", "model_name", "category", "date")
    search_fields = ("brand_product__startswith", "model__startswith", "category__startswith",)


"""registering Products module in admin panel"""
admin.site.register(Products, ProductsAdmin)
