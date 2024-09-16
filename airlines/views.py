from django.shortcuts import render, redirect

from .models import Flight, Passenger

def index(request):
    flights = Flight.objects.all()
    return render(request, "airlines/index.html", {
        "flights": flights
    })
    
    
def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    nonpassengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "airlines/flight.html", {
        "flight": flight,
        "nonpassengers": nonpassengers,
    })
    
    
def book(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    if request.method == "POST":
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return redirect("flight", flight_id=flight_id)
    
    return render(request, "airlines/book.html", {
        "flight": flight
    })