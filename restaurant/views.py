from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView

from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemAPIView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingAPIView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
