from django.urls import path

from blog_app.views import blog, blog_details

urlpatterns = [

    path('', blog, name='blog'),
    path('post-details/<int:pk>', blog_details, name='blog details'),

]
