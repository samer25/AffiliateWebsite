from django.urls import path

from product_app.views import products, ProductDetailView

urlpatterns = [

    path('', products, name='products'),
    path('details/<slug:slug>', ProductDetailView.as_view(), name='product details'),

]
