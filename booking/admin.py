from django.contrib import admin
from .models import Airline, Airplane, Airport, Flight, PlaneSeat, Person, Booking

admin.site.register(Airline)
admin.site.register(Airplane)
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(PlaneSeat)
admin.site.register(Person)
admin.site.register(Booking)
