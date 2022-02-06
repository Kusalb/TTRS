from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_admin = models.BooleanField('Admin', default=False)
    is_user = models.BooleanField('User', default=False)


# Create your models here.
class Tourism(models.Model):
    image = models.ImageField(default="def.png")
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    website = models.CharField(max_length=255,null=True)
    opening_hours = models.CharField(max_length=255,null=True)
    category = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6,null=True)
    latitude = models.DecimalField(max_digits=10,decimal_places=6, null=True)
    rating = models.FloatField()

