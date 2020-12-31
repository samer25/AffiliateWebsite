from django.contrib import admin

# Register your models here.
from blog_app.models import Blog, RelatedBlogProducts

"""Combining RelatedBlogProducts module with Blog module in admin panel   """


class RelatedBlogProductsInline(admin.StackedInline):
    model = RelatedBlogProducts


class BlogAdmin(admin.ModelAdmin):
    """Adding list display to show name fields in admin"""
    list_display = ("title", "description", "desc_min", "resources", "date")
    search_fields = ("title__startswith", "date__startswith",)
    inlines = [RelatedBlogProductsInline]


"""Register blog in admin page"""
admin.site.register(Blog, BlogAdmin)
