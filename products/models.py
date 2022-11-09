from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()


    image = models.ImageField(upload_to="proucts/images")
