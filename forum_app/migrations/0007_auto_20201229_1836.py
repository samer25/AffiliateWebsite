# Generated by Django 3.1.4 on 2020-12-29 18:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum_app', '0006_auto_20201229_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='views_count',
        ),
        migrations.AddField(
            model_name='forum',
            name='views_count',
            field=models.ManyToManyField(related_name='views', to=settings.AUTH_USER_MODEL),
        ),
    ]
