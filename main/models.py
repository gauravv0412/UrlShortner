from django.db import models
import datetime

# Create your models here.

class database(models.Model):
    
    shortened_url = models.CharField(max_length=8)
    actual_url = models.CharField(max_length=2048)
    num_clicks = models.IntegerField(default=0)
    tob = models.TimeField(auto_now=True)
    dob = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.shortened_url