# Generated by Django 3.1.4 on 2020-12-31 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profileuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
