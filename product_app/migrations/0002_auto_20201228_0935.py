# Generated by Django 3.1.4 on 2020-12-28 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='name_product',
            new_name='brand_product',
        ),
    ]
