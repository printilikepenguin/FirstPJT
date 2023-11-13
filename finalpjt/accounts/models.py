from django.db import models
from django.contrib.auth.models import AbstractUser
# from deposits.models import DepositProducts
# Create your models here.

class User(AbstractUser):
    family_name = models.CharField(max_length=20,unique=True)
    first_name = models.CharField(max_length=20,unique=True)
    age = models.IntegerField(default=20)
    email = models.CharField(max_length=50)
    seed_money = models.IntegerField(default=-1)
    salary = models.IntegerField(default=-1)
    # financial_products = models.ManyToManyField(DepositProducts, blank=True, related_name="joined")