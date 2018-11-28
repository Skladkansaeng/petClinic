from django.db import models
import datetime
from user.models import mypet as usermodel
# Create your models here.
class queue(models.Model):
    # pet_name = models.OneToOneField(usermodel, on_delete=models.CASCADE, primary_key=True )
    pet_name = models.ForeignKey(usermodel ,on_delete = models.CASCADE,default=5)
    pet_weight  = models.CharField(max_length=255, default='')
    pet_HeartRate = models.CharField(max_length=30, default='')
    pet_restRate =models.CharField(max_length=30, default='')
    pet_Dehydration = models.CharField(max_length=30, default='')
    pet_want = models.CharField(max_length=30, default='')
    veterinarian = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')

class medical(models.Model):
    pet_name = models.ForeignKey(usermodel, on_delete = models.CASCADE,default=5)
    medical_date = models.CharField(max_length=30,default=5)
    age = models.CharField(max_length=30,default='-')
    symptom = models.CharField(max_length=255)
    medicine = models.CharField(max_length=255)
    monation = models.CharField(max_length=255)
    veterinarian = models.CharField(max_length=255)

class vaccine(models.Model):
    pet_name = models.ForeignKey(usermodel, on_delete = models.CASCADE,default=5)
    vaccine_date = models.CharField(max_length=4,default=5)
    age = models.CharField(max_length=30,default='-')
    immunization = models.CharField(max_length=255)
    vaccine = models.CharField(max_length=255)
    dose = models.CharField(max_length=255)
    next_due = models.CharField(max_length=255)
    vaccine_time = models.CharField(max_length=4,default=5)
    veterinarian = models.CharField(max_length=255)

class appointment(models.Model):
    pet_name = models.ForeignKey(usermodel, on_delete = models.CASCADE,default=5)
    next_due =  models.CharField(max_length=255)
    username = models.CharField(max_length=30,default='')
    time = models.CharField(max_length=4,default=5)
    Description =  models.CharField(max_length=255)
