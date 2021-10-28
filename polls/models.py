from django.db import models

# Create your models here.
from rest_framework.authtoken.admin import User


class msg(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.CharField(max_length=20)
    text = models.CharField(max_length=1200)
    myDate = models.DateTimeField()