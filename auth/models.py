from django.db import models

from django.contrib.auth.models import User

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    

