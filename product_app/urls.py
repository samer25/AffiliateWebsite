from django.urls import path

from product_app.views import products, ProductDetailView
"""adding to url product view and details that taking slug"""
urlpatterns = [

    path('', products, name='products'),
    path('details/<slug:slug>', ProductDetailView.as_view(), name='product details'),

]
