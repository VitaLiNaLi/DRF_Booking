from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, generics
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Profile, Room, TypeOfRoom, Hotel, Booking
from rest_framework.generics import UpdateAPIView
from .serializers import ProfileSerializer, RoomSerializer, TypeOfRoomSerializer, HotelSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ReadOnlyModelViewSet


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')

        if User.objects.filter(username=username).exists():
            return Response({'message': 'Username already exists'},
                            status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)

        profile = Profile(user=user)
        if first_name:
            profile.first_name = first_name
        if last_name:
            profile.last_name = last_name
        profile.save()

        user.save()
        token.save()

        return Response({'token': token.key},
                        status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not User.objects.filter(username=username).exists():
            return Response({'message': 'Username does not exists'},
                            status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(username=username)

        if not user.check_password(password):
            return Response({'message': 'Incorrect password'},
                            status=status.HTTP_401_UNAUTHORIZED)

        token = Token.objects.get(user=user)

        return Response({'token': token.key},
                        status=status.HTTP_200_OK)


class ProfileUpdateView(UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


class ProfileViewSet(ReadOnlyModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs['username']
        user = User.objects.get(username=username)
        return Profile.objects.filter(user=user)


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class TypeOfRoomViewSet(viewsets.ModelViewSet):
    queryset = TypeOfRoom.objects.all()
    serializer_class = TypeOfRoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class RoomSearchViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    #search_filter = ['hotel']
    filterset_fields = ['hotel', 'typeOfRoom']


class RoomRetrievUpdateDestroy(generics.RetrieveDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]