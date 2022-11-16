# Generated by Django 3.2.9 on 2022-05-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_watchlist_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('bid', models.DecimalField(decimal_places=2, max_digits=32)),
            ],
        ),
    ]
