from datetime import datetime

from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=2000)


class Message(models.Model):
    value = models.CharField(max_length=10000)
    date = models.DateTimeField(default=datetime.now , blank = True)
    user = models.CharField(max_length=2000)
    room = models.CharField(max_length=2000)