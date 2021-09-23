from django.db import models

# Create your models here.
from django.contrib.auth.models import User

import datetime
from django.utils import timezone
class Photo(models.Model):
    image = models.ImageField(null=False, blank=False) #pip install pilow
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True) 


    def __str__(self):
        return self.description