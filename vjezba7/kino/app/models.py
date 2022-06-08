from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Projection(models.Model):
    movieName = models.TextField()
    screeningTime = models.TimeField()
    cinemaHallCapacity = models.IntegerField(default=20)

    def __str__(self):
        return 'name: %s , time: %s, seats: %s' %(self.movieName,self.screeningTime,self.cinemaHallCapacity)
        
   

class Ticket(models.Model):
    seatNumber = models.IntegerField(null=True)
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    movieName = models.ForeignKey(Projection, on_delete = models.CASCADE, null=True)

