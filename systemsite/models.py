from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.
User=settings.AUTH_USER_MODEL

class SiteSystem(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    
    
    
    class Meta:
        db_table='sitesystem'

    def delete_systemsite(self):
        return reverse('systemsite:delete',kwargs={'id':self.id})


    def update_systemsite(self):
        return reverse('systemsite:update',kwargs={'id':self.id})

    def __str__(self):
        return self.name




