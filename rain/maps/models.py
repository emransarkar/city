from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class MapData(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    
    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'id': self.id})