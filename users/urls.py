from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RegisterView, LoginView, ProfileUpdateView, ProfileViewSet, RoomViewSet, HotelViewSet, \
    TypeOfRoomViewSet, RoomSearchViewSet, BookingViewSet, RoomRetrievUpdateDestroy

router = DefaultRouter()
router.register(r'room', RoomViewSet)
router.register(r'hotel', HotelViewSet)
router.register(r'type', TypeOfRoomViewSet)
router.register(r'booking', BookingViewSet)

router.register(r'room_search', RoomSearchViewSet)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('delete_room/<int:pk>', RoomRetrievUpdateDestroy.as_view(), name='delete_room'),
    path('profile/<str:username>/', ProfileViewSet.as_view({'get': 'list'}), name='profile-list'),
    path('', include(router.urls)),
]





#urlpatterns = [
   # path('', include(router.urls)),
#]