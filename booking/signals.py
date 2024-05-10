from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FlightSchedule, Ticket
@receiver(post_save, sender=FlightSchedule)
def create_tickets(sender, instance, created, **kwargs):
    print('working')
    if created:
        # Create tickets for different classes
        aircraft = instance.airCraft
        econom_seats = aircraft.econom_class_seats
        premium_seats = aircraft.premium_class_seats
        business_seats = aircraft.business_class_seats

        # Create econom class tickets
        for i in range(econom_seats):
            seat_number = i + 1
            window_seat = seat_number == 1 or seat_number == aircraft.amount_of_columns_econom
            Ticket.objects.create(flight=instance, ticket_class='Econom', price=instance.price_for_econom, seat_number=seat_number, window_seat=window_seat)

        # Create premium class tickets
        for i in range(premium_seats):
            seat_number = i + 1
            window_seat = seat_number == 1 or seat_number == aircraft.amount_of_columns_premium
            Ticket.objects.create(flight=instance, ticket_class='Premium', price=instance.price_for_premium, seat_number=seat_number, window_seat=window_seat)

        # Create business class tickets
        for i in range(business_seats):
            seat_number = i + 1
            window_seat = seat_number == 1 or seat_number == aircraft.amount_of_columns_business
            Ticket.objects.create(flight=instance, ticket_class='Business', price=instance.price_for_business, seat_number=seat_number, window_seat=window_seat)
