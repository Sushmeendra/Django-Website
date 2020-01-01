from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import sys
from django.utils import timezone


# Create your models here.


class User(models.Model):
    user_Name = models.CharField(max_length=150, unique=True)
    user_DOB = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(99)])
    user_Email = models.EmailField()
    user_Password = models.CharField(max_length=20)
    users=models.Manager()

    def __str__(self):
        return self.user_Name


class Portfolio(models.Model):
    user_Portfolio = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    port_Name = models.CharField(max_length=50)
    ports=models.Manager()

    def __str__(self):
        return self.port_Name


class Investment(models.Model):
    investment_parent = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    investment_amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(sys.maxsize)])
    investment_date = models.DateField()
    investment_name = models.CharField(max_length=30, primary_key=True)
    return_rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)])
    investments = models.Manager()

    def __str__(self):
        return self.investment_name




