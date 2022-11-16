from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class auction(models.Model):
    user = models.CharField(max_length=64)
    title = models.CharField(max_length=128, null=False)
    description = models.CharField(max_length= 512, null=False)
    bid = models.DecimalField(max_digits=32, decimal_places=2, null=False)
    url = models.URLField(max_length=128)
    category = models.CharField(max_length=64)
    oc = models.BooleanField(default=True)
    winner = models.CharField(max_length=64, null=True)

class watchlist(models.Model):
    id = models.IntegerField(primary_key=True)
    listing = models.CharField(max_length=128)
    user = models.CharField(max_length=64)
    added = models.BooleanField(default=False)

class bid(models.Model):
    user = models.CharField(max_length=64)
    bid = models.DecimalField(max_digits=32, decimal_places=2, null=False)
    item = models.CharField(max_length=128, null=False)

class comment(models.Model):
    user = models.CharField(max_length=64)
    comment = models.CharField(max_length=512)
    title = models.CharField(max_length=128)
    heading = models.CharField(max_length=128)
