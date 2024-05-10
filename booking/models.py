from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from user.models import MyUser

# Create your models here.

class ManFact(models.Model):
    MANUFACTURER_CHOICES = [
        ('Airbus', 'Airbus'),
        ('Boeing', 'Boeing'),
        ('Bombardier', 'Bombardier'),
        ('Embraer', 'Embraer'),
        ('Lockheed Martin', 'Lockheed Martin'),
        ('Textron Aviation', 'Textron Aviation'),
        ('Mitsubishi Aircraft Corporation', 'Mitsubishi Aircraft Corporation'),
        ('Antonov', 'Antonov'),
        ('Saab', 'Saab'),
        ('Dassault Aviation', 'Dassault Aviation'),
        ('Tupolev', 'Tupolev'),
        ('Ilyushin', 'Ilyushin'),
        ('Aerospatiale', 'Aerospatiale'),
        ('British Aerospace', 'British Aerospace'),
        ('Fokker', 'Fokker'),
        ('McDonnell Douglas', 'McDonnell Douglas'),
        ('ATR', 'ATR'),
        ('Pilatus Aircraft', 'Pilatus Aircraft'),
        ('Cessna', 'Cessna'),
        ('Gulfstream Aerospace', 'Gulfstream Aerospace'),
        ('Piaggio Aerospace', 'Piaggio Aerospace'),
        ('Honda Aircraft Company', 'Honda Aircraft Company'),
        ('Diamond Aircraft Industries', 'Diamond Aircraft Industries'),
        ('Cirrus Aircraft', 'Cirrus Aircraft'),
        ('Emivest Aerospace', 'Emivest Aerospace'),
        ('Leonardo S.p.A.', 'Leonardo S.p.A.'),
        ('Kawasaki Heavy Industries', 'Kawasaki Heavy Industries'),
        ('Tecnam', 'Tecnam'),
        ('Beechcraft', 'Beechcraft'),
        ('Piper Aircraft', 'Piper Aircraft'),
        ('AgustaWestland', 'AgustaWestland'),
        ('Israel Aerospace Industries', 'Israel Aerospace Industries'),
        ('Groen Brothers Aviation', 'Groen Brothers Aviation'),
        ('PZL Świdnik', 'PZL Świdnik'),
        ('Kamov', 'Kamov'),
        ('Beriev', 'Beriev'),
        ('Harbin Aircraft Industry Group', 'Harbin Aircraft Industry Group'),
        ('Xi’an Aircraft Industrial Corporation', 'Xi’an Aircraft Industrial Corporation'),
        ('Shanghai Aircraft Manufacturing Factory', 'Shanghai Aircraft Manufacturing Factory'),
        ('Xi’an Aircraft Company', 'Xi’an Aircraft Company'),
        ('Shaanxi Aircraft Corporation', 'Shaanxi Aircraft Corporation'),
        ('Harbin Aircraft Manufacturing Corporation', 'Harbin Aircraft Manufacturing Corporation'),
        ('Shenyang Aircraft Corporation', 'Shenyang Aircraft Corporation'),
        ('Nanchang Aircraft Manufacturing Corporation', 'Nanchang Aircraft Manufacturing Corporation'),
        ('Jiangxi Hongdu Aviation Industry', 'Jiangxi Hongdu Aviation Industry'),
        ('Xian Aircraft Design Institute', 'Xian Aircraft Design Institute'),
        ('Nanchang Aircraft Company', 'Nanchang Aircraft Company'),
        ('Shanghai Aviation Industrial Company', 'Shanghai Aviation Industrial Company'),
        ('China Aviation Industry Corporation I', 'China Aviation Industry Corporation I'),
        ('China Aviation Industry Corporation II', 'China Aviation Industry Corporation II'),
        ('AVIC Aircraft', 'AVIC Aircraft'),
        ('AVIC General Aircraft', 'AVIC General Aircraft'),
        ('Chengdu Aircraft Industry Group', 'Chengdu Aircraft Industry Group'),
        ('AVIC Harbin Aircraft Industry Group', 'AVIC Harbin Aircraft Industry Group'),
        ('AVIC Helicopter', 'AVIC Helicopter'),
        ('AVIC Xi’an Aircraft Industry (Group) Company', 'AVIC Xi’an Aircraft Industry (Group) Company'),
        ('AVIC Xi’an Aircraft Industry Company Limited', 'AVIC Xi’an Aircraft Industry Company Limited'),
        ('AVIC Xian Aircraft Corporation', 'AVIC Xian Aircraft Corporation'),
        ('AVIC Nanchang Aircraft Corporation', 'AVIC Nanchang Aircraft Corporation'),
        ('AVIC Guizhou Aircraft Corporation', 'AVIC Guizhou Aircraft Corporation'),
        ('AVIC Harbin Aircraft Industry (Group) Company', 'AVIC Harbin Aircraft Industry (Group) Company'),
        ('AVIC Hongdu Aviation Industry Group', 'AVIC Hongdu Aviation Industry Group'),
        ('AVIC Shenyang Aircraft Corporation', 'AVIC Shenyang Aircraft Corporation'),
        ('AVIC Harbin Dongan Engine Manufacturing Company', 'AVIC Harbin Dongan Engine Manufacturing Company'),
        ('AVIC Aviation Engine Corporation', 'AVIC Aviation Engine Corporation'),
        ('AVIC Aero-Engine Controls Company', 'AVIC Aero-Engine Controls Company'),
        ('AVIC Flight Automatic Control Research Institute', 'AVIC Flight Automatic Control Research Institute'),
        ('AVIC Harbin Dongan Aero Engine Group', 'AVIC Harbin Dongan Aero Engine Group'),
        ('AVIC Harbin Aircraft Industry (Group) Co., Ltd.', 'AVIC Harbin Aircraft Industry (Group) Co., Ltd.'),
        ('AVIC Harbin Aviation Industry Group', 'AVIC Harbin Aviation Industry Group'),
        ('AVIC Aviation Industry Corporation of China', 'AVIC Aviation Industry Corporation of China'),
        ('AVIC Aircraft Co., Ltd.', 'AVIC Aircraft Co., Ltd.'),
        ('AVIC Changhe Aircraft Industries Corporation', 'AVIC Changhe Aircraft Industries Corporation'),
        ('AVIC Hafei Aviation Industry Company', 'AVIC Hafei Aviation Industry Company'),
        ('AVIC Commercial Aircraft Engine Company', 'AVIC Commercial Aircraft Engine Company'),
        ('AVIC Changhe Aviation Industry Corporation', 'AVIC Changhe Aviation Industry Corporation'),
        ('AVIC Harbin Aircraft Industry Group Company', 'AVIC Harbin Aircraft Industry Group Company'),
        ('AVIC Harbin Aircraft Corporation', 'AVIC Harbin Aircraft Corporation'),
        ('AVIC Harbin Turbine Engine Company', 'AVIC Harbin Turbine Engine Company'),
        ('AVIC Hanzhong Aircraft Industry Company', 'AVIC Hanzhong Aircraft Industry Company'),
        ('AVIC Nanchang Aircraft Manufacturing Corporation', 'AVIC Nanchang Aircraft Manufacturing Corporation'),
        ('AVIC Chengdu Aircraft Corporation', 'AVIC Chengdu Aircraft Corporation'),
        ('AVIC Shenyang Aircraft Corporation', 'AVIC Shenyang Aircraft Corporation'),
        ('AVIC Harbin Aircraft Manufacturing Corporation', 'AVIC Harbin Aircraft Manufacturing Corporation'),
        ('AVIC Changhe Aircraft Corporation', 'AVIC Changhe Aircraft Corporation'),
        ('AVIC Shaanxi Aircraft Corporation', 'AVIC Shaanxi Aircraft Corporation'),
        ('AVIC Chengdu Aircraft Industrial (Group) Company', 'AVIC Chengdu Aircraft Industrial (Group) Company'),
        ('AVIC Nanchang Aircraft Manufacturing Corporation', 'AVIC Nanchang Aircraft Manufacturing Corporation'),
        ('AVIC Nanchang Aircraft Corporation', 'AVIC Nanchang Aircraft Corporation'),
        ('AVIC Shenyang Aircraft Corporation', 'AVIC Shenyang Aircraft Corporation'),
        ('AVIC Xi’an Aircraft Industrial Corporation', 'AVIC Xi’an Aircraft Industrial Corporation'),
        ('AVIC Harbin Aircraft Industrial (Group) Company', 'AVIC Harbin Aircraft Industrial (Group) Company'),
    ]
    name = models.CharField(unique=True, null=False, max_length=100, choices=MANUFACTURER_CHOICES)

    def __str__(self) -> str:
        return f'{self.name}'


class AirCraft(models.Model):
    ac_Number = models.CharField(max_length=32, null=False)
    total_seats = models.PositiveIntegerField(null=False)
    manufacture = models.ForeignKey(to=ManFact, on_delete=models.PROTECT, null=False, related_name='mann')
    premium_class_seats = models.PositiveIntegerField(null=True)
    econom_class_seats = models.PositiveIntegerField(null=True)
    business_class_seats = models.PositiveIntegerField(null=True)
    amount_of_columns_premium = models.PositiveIntegerField(null=True)
    amount_of_columns_econom = models.PositiveIntegerField(null=True)
    amount_of_columns_business = models.PositiveIntegerField(null=True)

    def __str__(self) -> str:
        return f'{self.ac_Number} - {self.manufacture.name}'


class Country(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self) -> str:
        return self.name


class State(models.Model):
    statename = models.CharField(max_length=32, unique=True, null=False)
    country = models.ForeignKey(to=Country, related_name='country', null=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.statename


class Airport(models.Model):
    city = models.ForeignKey(related_name='port_loc', to=State, null=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.city.statename


class Route(models.Model):
    airport = models.ForeignKey(to=Airport, null=False, on_delete=models.CASCADE, related_name='airport')
    destination = models.ForeignKey(to=Airport, null=False, on_delete=models.CASCADE, related_name='destination')

    rout_code = models.CharField(max_length=16, null=False, unique=True)

    def clean(self):
        if self.airport_id == self.destination_id:
            raise ValidationError("Airport and destination cannot be the same.")

    def __str__(self) -> str:
        return self.rout_code


class FlightSchedule(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        ('JPY', 'Japanese Yen'),
        ('CNY', 'Chinese Yuan'),
    ]
    route = models.ForeignKey(to=Route, on_delete=models.CASCADE, related_name='route_of_flight', null=False)
    flightDate = models.DateField()
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    period = models.CharField(max_length=100, default='2h 30 m')
    airCraft = models.ForeignKey(to=AirCraft, on_delete=models.CASCADE, related_name='aircraft_sch')
    price_for_econom = models.PositiveIntegerField()
    price_for_premium = models.PositiveIntegerField()
    price_for_business = models.PositiveIntegerField()
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self) -> str:
        return f'{self.departure_time} - {self.arrival_time}, {self.route}'


class Ticket(models.Model):
    TICKET_CLASS_CHOICES = [
        ('Econom', 'Economy Class'),
        ('Premium', 'Premium Class'),
        ('Business', 'Business Class'),
    ]
    flight = models.ForeignKey(related_name='tickets', on_delete=models.CASCADE, to=FlightSchedule)
    ticket_class = models.CharField(max_length=10, choices=TICKET_CLASS_CHOICES)
    price = models.PositiveIntegerField()
    seat_number = models.PositiveIntegerField()
    window_seat = models.BooleanField(default=False)
    user = models.ForeignKey(MyUser, related_name='tickets', on_delete=models.CASCADE, null=True, blank=True)
    booked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.ticket_class} Ticket for {self.flight}'

