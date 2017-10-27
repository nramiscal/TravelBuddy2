# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import Trip
from ..user_app.models import User


def my_page(request):
    # Trip.objects.all().delete()

    data = {
    'my_trips': User.objects.get(id=request.session['id']).joins.all(),
    'other_trips': Trip.objects.exclude(joiners = request.session['id'])
    }

    return render(request, "trip_app/my_page.html", data)

def show(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    joiners = trip.joiners.all()

    return render(request, "trip_app/show.html", {"trip" : trip, "joiners" : joiners})


def join(request, trip_id, user_id):
    
    trip = Trip.objects.get(id=trip_id)
    user = User.objects.get(id=user_id)
    user.joins.add(trip) # OR trip.joins.add(user)
    return redirect("/my_page")


def add(request):
    return render(request, "trip_app/add.html")

def createTrip(request):
    print request.session['id']

    valid = Trip.objects.tripValidator(request.POST, request.session['id'])

    if valid[0]:
        return redirect("/my_page")
    else:
        for error in valid[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect("/add")

    return redirect("/add")
