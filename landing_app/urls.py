from django.urls import path

from landing_app.views import index, about
"""Adding to urls the home and about view"""
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),

]