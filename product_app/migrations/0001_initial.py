# Generated by Django 3.1.4 on 2020-12-28 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_product', models.ImageField(upload_to='image_products')),
                ('name_product', models.CharField(max_length=50)),
                ('description_product', models.TextField()),
                ('details_product', models.TextField()),
                ('link_product_amazon', models.URLField()),
            ],
        ),
    ]
