# Generated by Django 5.0.1 on 2024-03-20 15:45

import Petstagram.accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_petstagramuser_groups_petstagramuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='petstagramuser',
            managers=[
                ('objects', Petstagram.accounts.models.PetstagramUserManager()),
            ],
        ),
        migrations.AddField(
            model_name='petstagramuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='petstagramuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
