# Generated by Django 5.0.1 on 2024-01-29 11:27

import Petstagram.photos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(upload_to='pet_photos/', validators=[Petstagram.photos.models.image_size_less_than_5mb_validator]),
        ),
    ]
