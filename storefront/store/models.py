from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ForeignKey(Category)
    price = models.IntegerField()
    image = models.FileField(upload_to='var/www/media/')
    reviewlink = models.TextField()
    def __str__(self):
        return self.name