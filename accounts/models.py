from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
     user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='profile')
     phone=models.CharField(max_length=100,blank=True)
     location=models.CharField(max_length=100,blank=True)
     profile=models.ImageField(upload_to="users/%Y/%m",default='images/users/default/brand.png',null=True,blank=True)

     def __str__(self):
        return  f'{self.user}'
    
