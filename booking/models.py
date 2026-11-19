from django.db import models
from django.contrib.auth.models import User

class Airline(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Airplane(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='airplanes')
    model_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveIntegerField(default=120)

    def __str__(self):
        return f"{self.airline.code} - {self.model_name} ({self.registration_number})"

class Airport(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.code}), {self.city}"

class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='flights')
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='flights')
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Flight {self.flight_number}: {self.origin.code} -> {self.destination.code}"

class PlaneSeat(models.Model):
    SEAT_CLASSES = [
        ('Economy', 'Economy'),
        ('Business', 'Business'),
        ('First', 'First Class'),
    ]
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    seat_class = models.CharField(max_length=20, choices=SEAT_CLASSES, default='Economy')
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ('airplane', 'seat_number')

    def __str__(self):
        return f"{self.seat_number} ({self.seat_class}) on {self.airplane.model_name}"

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class Booking(models.Model):
    BOOKING_STATUS = [
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Pending', 'Pending'),
    ]
    booking_reference = models.CharField(max_length=20, unique=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='bookings')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='bookings')
    seat = models.ForeignKey(PlaneSeat, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=BOOKING_STATUS, default='Confirmed')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking {self.booking_reference} - {self.person} for {self.flight}"
