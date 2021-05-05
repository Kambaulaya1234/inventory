from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class Weapon(models.Model):
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    total=models.IntegerField(default=1)
    image=models.ImageField()

    
    def  delete_weapon(self):
        return reverse('delete_weapon',kwargs={'id':self.id})

    def update_weapon(self):
        return reverse('update_weapon',kwargs={'id':self.id})

    class Meta:
        db_table='weapons'


    def __str__(self):
        return self.name



