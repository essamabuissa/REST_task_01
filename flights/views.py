from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightSerializer , BookingSerializer
from datetime import datetime

class FlightList(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class BookingList(ListAPIView):
    queryset = Booking.objects.filter(date__gt = datetime.today())
    serializer_class = BookingSerializer
