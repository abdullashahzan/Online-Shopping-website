# Generated by Django 3.2.9 on 2022-05-13 19:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_comment_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='heading',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
    ]
