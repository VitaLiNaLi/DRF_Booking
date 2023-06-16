from django.contrib import admin
from .models import Profile, Room, Hotel, TypeOfRoom, Booking

# Register your models here.
admin.site.register(Profile)
admin.site.register(TypeOfRoom)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)
