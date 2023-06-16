from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Profile, TypeOfRoom, Room, Hotel, Booking


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class TypeOfRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeOfRoom
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    Hotels = HotelSerializer(many=False, read_only=True)
    TypeOfRooms = TypeOfRoomSerializer(many=False, read_only=True)
    class Meta:
        model = Booking
        fields = '__all__'