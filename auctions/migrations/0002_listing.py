# Generated by Django 4.1.5 on 2023-01-19 07:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
                ('starting_bid', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(max_length=32)),
                ('image_url', models.TextField(blank=True, validators=[django.core.validators.URLValidator()])),
            ],
        ),
    ]
