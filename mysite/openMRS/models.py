from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Member(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    dateofbirth=models.DateField(null=True)
    gender=models.CharField(max_length=255,default='')
    address = models.CharField(max_length=100, default='')
    phonenumber=models.CharField(max_length=15,default='')
    email=models.CharField(max_length=255,default='')
    nationality=models.CharField(max_length=255,default='')
    maritalstatus=models.CharField(max_length=255,default='')
    occupation=models.CharField(max_length=255,default='')
    emergencycontact=models.CharField(max_length=255,default='')
    insuranceinformation=models.CharField(max_length=255,default='')
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def _str_(self):
        return self.title    
