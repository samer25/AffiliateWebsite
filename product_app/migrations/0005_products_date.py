# Generated by Django 3.1.4 on 2020-12-29 21:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0004_auto_20201228_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
