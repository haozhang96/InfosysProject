from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(primary_key=True, max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.ForeignKey("Address", on_delete=models.CASCADE)
    billing_info = models.ForeignKey("BillingInfo", on_delete=models.CASCADE)

class Address(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

class BillingInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=20)
    expiration_date = models.CharField(max_length=20) # models.DateTimeField()
    address = models.ForeignKey("Address", on_delete=models.CASCADE)
