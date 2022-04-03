from django.db import models
from models import Node

class Pollution_Data(models.Model):
    data_Id = models.AutoField(primary_key=True)
    node_Id = models.ForeignKey(Node, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=None)
    mq135 = models.FloatField(blank=True, default=0)
    mq5 = models.FloatField(blank=True, default=0)
    mq7 = models.FloatField(blank=True, default=0)
    temp = models.FloatField(blank=True, default=0)
    humidity = models.FloatField(blank=True, default=0)
    alert=models.BooleanField(default=False)
    def __str__(self):
        return str(self.datetime)

class Node(models.Model):
    node_Id = models.AutoField(primary_key=True)
    installedDate = models.DateTimeField(default=None)
    isMQ135 = models.BooleanField(default=False)
    isMQ5 = models.BooleanField(default=False)
    isMQ7 = models.BooleanField(default=False)
    isDHT = models.BooleanField(default=False)
    latitude = models.FloatField(blank=True, default=0)
    longitude = models.FloatField(blank=True, default=0)
    def __str__(self):
        return str(self.datetime)