from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ProfileUser(models.Model):
    """Profile Model with relationship with User"""
    email = models.EmailField(blank=False, unique=True)
    name = models.CharField(max_length=10, blank=True)
    profile_pic = models.ImageField(upload_to='profile_img', default='default.png', blank=True)
    bio = models.TextField(blank=True, )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
