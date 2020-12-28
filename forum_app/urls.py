from django.urls import path

from forum_app.views import forum

urlpatterns = [
    path('', forum, name='forum'),

]
