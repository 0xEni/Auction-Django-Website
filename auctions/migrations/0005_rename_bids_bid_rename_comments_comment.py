# Generated by Django 4.1.5 on 2023-01-22 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_comments_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bids',
            new_name='Bid',
        ),
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]