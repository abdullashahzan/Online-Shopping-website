# Generated by Django 3.2.9 on 2022-05-12 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_auction_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='bid',
            field=models.DecimalField(decimal_places=2, max_digits=32),
        ),
    ]
