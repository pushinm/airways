from rest_framework import serializers
from .models import FlightSchedule, State, Airport, Ticket
from user.models import MyUser, Profile


class FlightSerializer(serializers.ModelSerializer):
    route_code = serializers.CharField(source='route.rout_code', read_only=True)

    class Meta:
        model = FlightSchedule
        fields = ['route_code', 'departure_time', 'arrival_time']


class FlightDetailSerializer(serializers.ModelSerializer):
    route_code = serializers.CharField(source='route.rout_code', read_only=True)
    airCraft = serializers.CharField(source='aircraft.')

    class Meta:
        model = FlightSchedule
        fields = ['route_code', 'departure_time', 'arrival_time', ]


class FlightScheduleSerializer(serializers.ModelSerializer):
    city1 = serializers.CharField(source='route.airport', read_only=True)
    city2 = serializers.CharField(source='route.destination', read_only=True)

    class Meta:
        model = FlightSchedule
        fields = ['id', 'route', 'flightDate', 'departure_time', 'arrival_time', 'airCraft', 'price_for_econom',
                  'price_for_premium', 'price_for_business', 'currency', 'city1', 'city2']


class StateSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.name', read_only=True)

    class Meta:
        model = State
        fields = ['id', 'statename']


class ProfileSerializer(serializers.ModelSerializer):
    profile = serializers.CharField(source='user.email')
    full_name = serializers.CharField(source='user.full_name')

    class Meta:
        model = Profile
        fields = ['phone_number']


class MyUserSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer(source='user.profile')  # Specify the source explicitly

    class Meta:
        model = MyUser
        fields = ['full_name', 'email', 'user_profile']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
