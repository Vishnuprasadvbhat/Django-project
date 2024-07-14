from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    # it is the standard length of the image urls
    image_url = models.CharField(max_length=2083)
# manage.py makemigrations
# python manage.py migrate


class Offers(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=1024)
    discount = models.FloatField()
