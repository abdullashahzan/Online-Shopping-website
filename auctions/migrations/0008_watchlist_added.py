# Generated by Django 3.2.9 on 2022-05-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20220513_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='added',
            field=models.BooleanField(default=False),
        ),
    ]