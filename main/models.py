from django.db import models

# Create your models here.

class Database(models.Model):
    
    shortened_url = models.CharField(max_length=16, blank = True, primary_key = True)
    actual_url = models.URLField(max_length=2048)
    is_private = models.BooleanField(default=False)
    num_clicks = models.IntegerField(default=0)
    tom = models.TimeField(auto_now_add=True)
    dom = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.shortened_url

