from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.user



class TypeOfRoom(models.Model):
    typeOfRoom = models.CharField(max_length=255)


    def __str__(self):
        return self.typeOfRoom


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    adress = models.CharField(max_length=255)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bed = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    typeOfRoom = models.ForeignKey(TypeOfRoom, on_delete=models.CASCADE)


class Booking(models.Model):
    room = models.IntegerField()
    #hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    #typeOfRoom = models.ForeignKey(TypeOfRoom, on_delete=models.CASCADE)
    beginDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField(auto_now_add=True)




