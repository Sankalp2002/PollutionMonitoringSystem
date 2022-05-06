from django.db import models 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
from datetime import datetime as dt

class Node(models.Model):
    node_Id = models.AutoField(primary_key=True)
    installedDate = models.DateField(default=date.today())
    mq135 = models.FloatField(blank=True, default=0)
    location=models.CharField(max_length=128, help_text="Enter location of the node",blank=True,default="None")
    alert=models.BooleanField(default=False)
    macAddress=models.CharField(max_length=128,blank=False,unique=True)
    def __str__(self):
        return str(self.node_Id)

class Pollution_Data(models.Model):
    data_Id = models.AutoField(primary_key=True)
    datetimestamp = models.DateTimeField(default=dt.now)
    mq135 = models.FloatField(blank=True, default=0)
    macAddress=models.ForeignKey(Node,to_field='macAddress', on_delete=models.CASCADE,default="None")
    def __str__(self):
        return str(self.datetimestamp)
