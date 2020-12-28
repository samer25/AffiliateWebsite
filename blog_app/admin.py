from django.contrib import admin

# Register your models here.
from blog_app.models import Blog, RelatedBlogProducts

admin.site.register(Blog)
admin.site.register(RelatedBlogProducts)
