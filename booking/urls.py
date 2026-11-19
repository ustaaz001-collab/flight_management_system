from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # Airlines
    path('airlines/', views.list_airline, name='list_airline'),
    path('airlines/add/', views.create_airline, name='create_airline'),
    path('airlines/delete/<int:pk>/', views.delete_airline, name='delete_airline'),

    # Airplanes
    path('airplanes/', views.list_airplane, name='list_airplane'),
    path('airplanes/add/', views.create_airplane, name='create_airplane'),
    path('airplanes/delete/<int:pk>/', views.delete_airplane, name='delete_airplane'),

    # Airports
    path('airports/', views.list_airport, name='list_airport'),
    path('airports/add/', views.create_airport, name='create_airport'),
    path('airports/delete/<int:pk>/', views.delete_airport, name='delete_airport'),

    # Flights
    path('flights/', views.list_flight, name='list_flight'),
    path('flights/add/', views.create_flight, name='create_flight'),
    path('flights/delete/<int:pk>/', views.delete_flight, name='delete_flight'),

    # Plane Seats
    path('seats/', views.list_seat, name='list_seat'),
    path('seats/add/', views.create_seat, name='create_seat'),
    path('seats/delete/<int:pk>/', views.delete_seat, name='delete_seat'),

    # Persons
    path('persons/', views.list_person, name='list_person'),
    path('persons/add/', views.create_person, name='create_person'),
    path('persons/delete/<int:pk>/', views.delete_person, name='delete_person'),

    # Bookings
    path('bookings/', views.list_booking, name='list_booking'),
    path('bookings/add/', views.create_booking, name='create_booking'),
    path('bookings/delete/<int:pk>/', views.delete_booking, name='delete_booking'),
]
