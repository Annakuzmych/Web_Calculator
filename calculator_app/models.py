from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager

class ProUser(AbstractUser): #28739f99_0_169
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

class CalculationHistory(models.Model):
    user = models.ForeignKey(ProUser, on_delete=models.CASCADE, default=1)
    expression = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

class ConversionHistory(models.Model):
    user = models.ForeignKey(ProUser, on_delete=models.CASCADE, default=1)
    number = models.CharField(max_length=100)
    from_base = models.IntegerField()
    to_base = models.IntegerField()
    result = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)



