from django.urls import path

from blog_app.views import blog, BlogDetailView

urlpatterns = [

    path('', blog, name='blog'),
    path('post-details/<slug:slug>', BlogDetailView.as_view(), name='blog details'),

]
