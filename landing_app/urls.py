from django.urls import path

from landing_app.views import index, about

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),

]