from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import FlightSchedule, Ticket, State
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from django.views import View
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .serializers import MyUserSerializer


# Create your views here.


class FlightsPagination(PageNumberPagination):
    page_size = 15


class FlightList(ListAPIView):
    serializer_class = FlightSerializer
    queryset = FlightSchedule.objects.all()


class AvailableFlightProposalsAPIView(ListAPIView):
    serializer_class = FlightScheduleSerializer

    def get_queryset(self):
        # Retrieve query parameters from the request
        departure_city_id = self.request.data.get('departure_city_id')
        print(departure_city_id)
        arrival_city_id = self.request.data.get('arrival_city_id')
        print(arrival_city_id)
        departure_date = self.request.data.get('departure_date')

        # Convert departure_date string to a date object
        departure_date = timezone.datetime.strptime(departure_date, '%Y-%m-%d').date()
        min_price = self.request.data.get('min')
        max_price = self.request.data.get('max')
        queryset = FlightSchedule.objects.filter(
            route__airport__city_id=departure_city_id,
            route__destination__city_id=arrival_city_id,
            flightDate=departure_date
        )
        if min_price is not None and max_price is not None:
            queryset = queryset.filter(price_for_econom__gte=min_price)
            queryset = queryset.filter(price_for_business__lte=max_price)
            return queryset

        # Filter FlightSchedule objects based on the provided parameters

        return queryset


class AirportInfoView(View):
    def get(self, request):
        airport_data = []

        # Query all airports with their city and country information
        airports = Airport.objects.select_related('city__country').all()

        # Iterate through each airport to construct the response data
        for airport in airports:
            airport_info = {
                'airport_id': airport.id,
                'city_id': airport.city.id,
                'country_id': airport.city.country.id,
                'airport_name': airport.city.statename,
                'country_name': airport.city.country.name,
            }
            airport_data.append(airport_info)

        return JsonResponse(airport_data, safe=False)


class FlightDetailView(APIView):
    def get(self, request):
        flight_id = request.data.get('flight_id')
        tickets_data = []

        # Query all tickets for the specified flight
        tickets = Ticket.objects.filter(flight_id=flight_id)

        # Iterate through each ticket to construct the response data
        for ticket in tickets:
            ticket_info = {
                'tiket_id': ticket.id,
                'ticket_class': ticket.ticket_class,
                'price': ticket.price,
                'seat_number': ticket.seat_number,
                'window_seat': ticket.window_seat,
                'booked': ticket.booked,
                'period': ticket.flight.period,
            }
            tickets_data.append(ticket_info)

        return Response(tickets_data)


@api_view(['POST'])
def book_ticket(request):
    ticket_id = request.data.get('ticket_id')
    auth_header = request.headers.get('Authorization')

    if auth_header is not None:
        token_string = auth_header.split(' ')[1]
    else:
        return Response({"detail": "Authorization header not provided"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        token = Token.objects.get(key=token_string)
        user_id = token.user.id
    except Token.DoesNotExist:
        return Response({"detail": "Token is invalid"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        # Retrieve the ticket
        ticket = Ticket.objects.get(id=ticket_id)

        # Check if the ticket is already booked
        if ticket.booked:
            return Response({"detail": "Ticket is already booked"}, status=status.HTTP_400_BAD_REQUEST)

        # Book the ticket for the user
        ticket.user_id = user_id
        ticket.booked = True
        ticket.save()
        serializer = TicketSerializer(ticket)
        all_data = [{
            'full_name': ticket.user.full_name,
            'email': ticket.user.email,
            'flight_date': ticket.flight.flightDate,
            'city1': str(ticket.flight.route.airport),
            'city2': str(ticket.flight.route.destination),
            'period': ticket.flight.period,
        }, serializer.data]
        return Response({'data': all_data, "detail": "Ticket booked successfully"}, status=status.HTTP_200_OK)
    except Ticket.DoesNotExist:
        return Response({"detail": "Ticket not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def my_tickets(request):
    auth_header = request.headers.get('Authorization')

    if auth_header is not None:
        token_string = auth_header.split(' ')[1]
    else:
        return Response({"detail": "Authorization header not provided"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        token = Token.objects.get(key=token_string)
        user_id = token.user.id

        # Filter tickets booked by the user
        tickets = Ticket.objects.filter(user_id=user_id)
        ticket_data = []

        for ticket in tickets:
            ticket_data.append({
                'id': ticket.id,
                'date': ticket.flight.flightDate,
                'departure_time': ticket.flight.departure_time,
                'arrival_time': ticket.flight.arrival_time,
                'city1': str(ticket.flight.route.airport),
                'city2': str(ticket.flight.route.destination),
                'period': ticket.flight.period,
            })

        return Response(ticket_data)

    except Token.DoesNotExist:
        return Response({"detail": "Token is invalid"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def booked_ticket_detail(request):
    ticket_id = request.data.get('ticket_id')
    auth_header = request.headers.get('Authorization')

    if auth_header is not None:
        token_string = auth_header.split(' ')[1]
    else:
        return Response({"detail": "Authorization header not provided"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        token = Token.objects.get(key=token_string)
        user_id = token.user.id
    except Token.DoesNotExist:
        return Response({"detail": "Token is invalid"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        # Retrieve the ticket
        ticket = Ticket.objects.get(id=ticket_id)
        if ticket.user.id == user_id:
            ticket.user_id = user_id
            ticket.booked = True
            ticket.save()
            serializer = TicketSerializer(ticket)
            all_data = [{
                'full_name': ticket.user.full_name,
                'email': ticket.user.email,
                'flight_date': ticket.flight.flightDate,
                'city1': str(ticket.flight.route.airport),
                'city2': str(ticket.flight.route.destination),
                'period': ticket.flight.period,
            }, serializer.data]
            return Response({'data': all_data, "detail": "hello"}, status=status.HTTP_200_OK)
        else:
            return Response('mismatch user and ticket')
    except Ticket.DoesNotExist:
        return Response({"detail": "Ticket not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def saved_tickets(request):
    request_list = request.data.get('list')
    # Remove trailing comma and split the string by commas
    id_strings = request_list.rstrip(',').split(',')

    # Convert each ID string to an integer and put it into a list
    id_list = [int(id_str) for id_str in id_strings]
    ticket_data = []
    for ticket in id_list:
        t = Ticket.objects.get(id=ticket)
        ticket_data.append({
            'id': t.id,
            'date': t.flight.flightDate,
            'departure_time': t.flight.departure_time,
            'arrival_time': t.flight.arrival_time,
            'city1': str(t.flight.route.airport),
            'city2': str(t.flight.route.destination),
            'period': t.flight.period,
        })
    return Response(data=ticket_data)
