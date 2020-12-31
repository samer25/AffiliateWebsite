from django.contrib import admin

from .models import Forum, Comment

"""Combining Forum with comments in admin panel """


class CommentInline(admin.StackedInline):
    model = Comment


class ForumAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "created_at")
    search_fields = ("user__startswith", "title__startswith", "created_at__startswith",)
    inlines = [CommentInline]


"""registering Forum in admin panel"""
admin.site.register(Forum, ForumAdmin)
