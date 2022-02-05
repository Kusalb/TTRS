from django.db import models

# Create your models here.
class Accomodation(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    website = models.CharField(max_length=255,null=True)
    opening_hours = models.CharField(max_length=255,null=True)
    category = models.CharField(max_length=255,null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=3,null=True)
    latitude = models.DecimalField(max_digits=10,decimal_places=3, null=True)

