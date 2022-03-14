from email import message
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    mobno=models.CharField(max_length=50)
    message=models.CharField(max_length=500)
    
    def __str__(self):
        return "%s"%(self.name)
    