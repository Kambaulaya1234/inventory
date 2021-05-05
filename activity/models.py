from django.db import models
from django.conf import settings
from weapon.models import Weapon
from systemsite.models import SiteSystem
from django.urls import reverse
User=settings.AUTH_USER_MODEL

# Create your models here.
class Activity(models.Model):
    guard=models.ForeignKey(User,on_delete=models.CASCADE)
    weapon=models.ForeignKey(Weapon,on_delete=models.CASCADE)
    site=models.ForeignKey(SiteSystem,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    class Meta:
        db_table='activities'

    def delete_activity(self):
        return reverse('activity:delete',kwargs={'id':self.id})

    def update_activity(self):
        return reverse('activity:update',kwargs={'id':self.id})


    def verify_activity(self):
        return reverse('activity:verify',kwargs={'id':self.id})