from django.db import models 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date, datetime
from django.utils import timezone

class Node(models.Model):
    node_Id = models.AutoField(primary_key=True)
    installedDate = models.DateField(default=date.today())
    isMQ135 = models.BooleanField(default=False)
    isMQ5 = models.BooleanField(default=False)
    isMQ7 = models.BooleanField(default=False)
    mq135 = models.FloatField(blank=True, default=0)
    mq5 = models.FloatField(blank=True, default=0)
    mq7 = models.FloatField(blank=True, default=0)
    latitude = models.FloatField(blank=True, default=0)
    longitude = models.FloatField(blank=True, default=0)
    alert=models.BooleanField(default=False)
    def __str__(self):
        return str(self.datetime)

class Pollution_Data(models.Model):
    data_Id = models.AutoField(primary_key=True)
    node_Id = models.ForeignKey(Node, on_delete=models.CASCADE,default=0)
    datetime = models.DateTimeField(default=timezone.now)
    mq135 = models.FloatField(blank=True, default=0)
    mq5 = models.FloatField(blank=True, default=0)
    mq7 = models.FloatField(blank=True, default=0)
    def __str__(self):
        return str(self.datetime)
