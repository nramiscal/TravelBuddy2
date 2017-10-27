# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from ..user_app.models import User

now = str(datetime.now())

class TripManager(models.Manager):
    def tripValidator(self, form, user_id):
        place = form['place']
        desc = form['desc']
        startDate = form['startDate']
        endDate = form['endDate']

        errors = []

        if len(place) < 1:
            errors.append("Please enter a destination.")
        if len(desc) < 1:
            errors.append("Please enter a description.")
        if not startDate:
            errors.append("Please choose a departure date.")
        elif startDate < now:
            errors.append("Departure date cannot be in the past.")
        if not endDate:
            errors.append("Please choose a return date.")
        elif endDate < startDate:
            errors.append("Return date cannot be before departure date.")

        if len(errors) > 0:
            return (False, errors)
        else:
            trip = Trip.objects.create(place = place, desc = desc, startDate = startDate, endDate = endDate, planner_id=user_id)

            user = User.objects.get(id=user_id)
            user.joins.add(trip)

            return (True, trip)


class Trip(models.Model):
    place = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    planner = models.ForeignKey(User, related_name = "trips")
    joiners = models.ManyToManyField(User, related_name = "joins")
    objects = TripManager()

    def __repr__(self):
        return "<Trip {} {}>".format(self.id, self.place)
