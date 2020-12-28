from django.urls import path

from product_app.views import products, product_details

urlpatterns = [

    path('', products, name='products'),
    path('details/<int:pk>', product_details, name='product details'),

]
