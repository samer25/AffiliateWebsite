# Generated by Django 3.1.4 on 2020-12-31 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_relatedblogproducts_blog_rel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relatedblogproducts',
            name='blog_product',
        ),
    ]
