from django.db import models
import datetime
# Create your models here
class staff(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    tel = models.CharField(max_length=10)
    email = models.EmailField(default="")
    status = models.CharField(max_length=7)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name+self.surname
