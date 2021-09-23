from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)