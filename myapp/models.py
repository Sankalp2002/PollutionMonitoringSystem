from django.db import models 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
from datetime import datetime as dt

class Node(models.Model):
    node_Id = models.AutoField(primary_key=True)
    installedDate = models.DateField(default=date.today())
    mq135 = models.FloatField(blank=True, default=0)
    location=models.CharField(max_length=128, help_text="Enter location of the node",blank=False,default="None")
    alert=models.BooleanField(default=False)
    def __str__(self):
        return str(self.node_Id)

class Pollution_Data(models.Model):
    data_Id = models.AutoField(primary_key=True)
    node_Id = models.ForeignKey(Node, on_delete=models.CASCADE,default=0)
    datetimestamp = models.DateTimeField(default=dt.now)
    mq135 = models.FloatField(blank=True, default=0)
    def __str__(self):
        return str(self.datetimestamp)
