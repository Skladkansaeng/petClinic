from django.db import models
import datetime
# Create your models here
class user(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    tel = models.CharField(max_length=10)
    email = models.EmailField(default="")
    username = models.CharField(max_length=30,default='')
    password = models.CharField(max_length=10,default='')
    def __str__(self):
        return self.name+self.surname

class mypet(models.Model):
    user = models.ForeignKey(user, on_delete = models.CASCADE,default=5)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    birthDate = models.DateField(default = datetime.date.today)
    age = models.CharField(max_length=2,default = '')
    breed = models.CharField(max_length=30,default = 0)
    sickness = models.CharField(max_length=40,default = 0)
    def __str__(self):
        return self.name
