from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Airline, Airplane, Airport, Flight, PlaneSeat, Person, Booking
from .forms import (
    AirlineForm, AirplaneForm, AirportForm, 
    FlightForm, PlaneSeatForm, PersonForm, BookingForm
)

@login_required
def dashboard(request):
    context = {
        'total_airlines': Airline.objects.count(),
        'total_airplanes': Airplane.objects.count(),
        'total_airports': Airport.objects.count(),
        'total_flights': Flight.objects.count(),
        'total_seats': PlaneSeat.objects.count(),
        'total_persons': Person.objects.count(),
        'total_bookings': Booking.objects.count(),
        'recent_bookings': Booking.objects.order_by('-booking_date')[:5],
    }
    return render(request, 'dashboard.html', context)

@login_required
def list_airline(request):
    query = request.GET.get('q', '')
    airlines = Airline.objects.filter(name__icontains=query).order_by('name')
    paginator = Paginator(airlines, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'airline/list_airline.html', {'page_obj': page_obj, 'query': query})

@login_required
def create_airline(request):
    form = AirlineForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Airline created successfully.")
        return redirect('booking:list_airline')
    return render(request, 'airline/airline_form.html', {'form': form})

@login_required
def delete_airline(request, pk):
    airline = get_object_or_404(Airline, pk=pk)
    if request.method == 'POST':
        airline.delete()
        messages.success(request, "Airline deleted successfully.")
        return redirect('booking:list_airline')
    return render(request, 'airline/delete_airline.html', {'object': airline})

@login_required
def list_airplane(request):
    query = request.GET.get('q', '')
    airplanes = Airplane.objects.filter(model_name__icontains=query).order_by('model_name')
    paginator = Paginator(airplanes, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'airplane/list_airplane.html', {'page_obj': page_obj, 'query': query})

@login_required
def create_airplane(request):
    form = AirplaneForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Airplane added successfully.")
        return redirect('booking:list_airplane')
    return render(request, 'airplane/airplane_form.html', {'form': form})

@login_required
def delete_airplane(request, pk):
    airplane = get_object_or_404(Airplane, pk=pk)
    if request.method == 'POST':
        airplane.delete()
        messages.success(request, "Airplane deleted successfully.")
        return redirect('booking:list_airplane')
    return render(request, 'airplane/delete_airplane.html', {'object': airplane})

@login_required
def list_airport(request):
    query = request.GET.get('q', '')
    airports = Airport.objects.filter(name__icontains=query) | Airport.objects.filter(code__icontains=query)
    paginator = Paginator(airports.distinct(), 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'airport/list_airport.html', {'page_obj': page_obj, 'query': query})

@login_required
def create_airport(request):
    form = AirportForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Airport added successfully.")
        return redirect('booking:list_airport')
    return render(request, 'airport/airport_form.html', {'form': form})

@login_required
def delete_airport(request, pk):
    airport = get_object_or_404(Airport, pk=pk)
    if request.method == 'POST':
        airport.delete()
        messages.success(request, "Airport deleted successfully.")
        return redirect('booking:list_airport')
    return render(request, 'airport/delete_airport.html', {'object': airport})

@login_required
def list_flight(request):
    query = request.GET.get('q', '')
    flights = Flight.objects.filter(flight_number__icontains=query).order_by('-departure_time')
    paginator = Paginator(flights, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'flight/list_flight.html', {'page_obj': page_obj, 'query': query})

@login_required
def create_flight(request):
    form = FlightForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Flight scheduled successfully.")
        return redirect('booking:list_flight')
    return render(request, 'flight/flight_form.html', {'form': form})

@login_required
def delete_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == 'POST':
        flight.delete()
        messages.success(request, "Flight cancelled/deleted successfully.")
        return redirect('booking:list_flight')
    return render(request, 'flight/delete_flight.html', {'object': flight})

@login_required
def list_seat(request):
    query = request.GET.get('q', '')
    seats = PlaneSeat.objects.filter(seat_number__icontains=query).order_by('airplane', 'seat_number')
    paginator = Paginator(seats, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'seat/list_seat.html', {'page_obj': page_obj, 'query': query})

@login_required
def create_seat(request):
    form = PlaneSeatForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Plane seat added successfully.")
        return redirect('booking:list_seat')
    return render(request, 'seat/seat_form.html', {'form': form})

@login_required
def delete_seat(request, pk):
    seat = get_object_or_404(PlaneSeat, pk=pk)
    if request.method == 'POST':
        seat.delete()
        messages.success(request, "Seat removed successfully.")
        return redirect('booking:list_seat')
    return render(request, 'seat/delete_seat.html', {'object': seat})

@login_required
def list_person(request):
    query = request.GET.get('q', '')
    persons = Person.objects.filter(first_name__icontains=query) | Person.objects.filter(last_name__icontains=query)
    paginator = Paginator(persons.distinct(), 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'person/list_person.html', {'page_obj': page_obj, 'query': query})

@login_required
def create_person(request):
    form = PersonForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Passenger profile created successfully.")
        return redirect('booking:list_person')
    return render(request, 'person/person_form.html', {'form': form})

@login_required
def delete_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        messages.success(request, "Passenger profile deleted successfully.")
        return redirect('booking:list_person')
    return render(request, 'person/delete_person.html', {'object': person})

@login_required
def list_booking(request):
    query = request.GET.get('q', '')
    bookings = Booking.objects.filter(booking_reference__icontains=query).order_by('-booking_date')
    paginator = Paginator(bookings, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'booking/list_booking.html', {'page_obj': page_obj, 'query': query})

@login_required
def create_booking(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Booking confirmed successfully.")
        return redirect('booking:list_booking')
    return render(request, 'booking/booking_form.html', {'form': form})

@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking cancelled/deleted successfully.")
        return redirect('booking:list_booking')
    return render(request, 'booking/delete_booking.html', {'object': booking})
