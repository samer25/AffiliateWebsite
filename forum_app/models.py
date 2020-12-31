from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect
from django.utils.text import slugify
import time
from django.urls import reverse

"""Creating Forum Model that users can create Questions and Comment that users cant answer the Question that have 
relationship with Forum """


class Forum(models.Model):
    """creating model for forum question with slug for url view cont """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    desc = models.TextField()
    views_count = models.ManyToManyField(User, related_name='views')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """saving slug title + time """
        if self.pk is None:
            self.slug = slugify(self.title) + '-' + time.strftime("%Y%m%d%H%M%S")
        super(Forum, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """getting url after success creating question"""
        return reverse('forum')


class Comment(models.Model):
    """creating comment for question that the users asked  have relation ship with user model and forum model that we
    can know how comment the question and to know that comment is answered to what question"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    desc = models.TextField()
    likes = models.ManyToManyField(User, related_name='like')
    dislikes = models.ManyToManyField(User, related_name='dislike')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """getting url after success creating comment and creating  slug """
        return reverse('forum-detail', kwargs={'slug': self.forum.slug})
