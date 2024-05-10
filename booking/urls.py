from django.urls import path
from .views import (FlightList, AvailableFlightProposalsAPIView,
                    AirportInfoView, FlightDetailView, book_ticket,
                    my_tickets, booked_ticket_detail, saved_tickets)

urlpatterns = [
    path('schedule/', FlightList.as_view()), # Xamma reyslar listi
    path('available/', AvailableFlightProposalsAPIView.as_view()), #filtirlangan reyslar list
    path('cities/', AirportInfoView.as_view()), #shaharlar/airportlar listi
    path('flight-detail/', FlightDetailView.as_view()), # Reys xaqida koproq detallar
    path('book/', book_ticket), # ticket booking
    path('user-tickets/', my_tickets),
    path('ticket-detail/', booked_ticket_detail),
    path('saved/', saved_tickets),
]