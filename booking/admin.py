from django.contrib import admin
from .models import ManFact, AirCraft, Route, FlightSchedule, Country, State, Airport, Ticket
# Register your models here.

admin.site.register(ManFact)
admin.site.register(AirCraft)
admin.site.register(Route)
admin.site.register(FlightSchedule)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Airport)
admin.site.register(Ticket)