# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
from ..trip_app.models import Trip

def index(request):
    # User.objects.all().delete()
    return render(request, "user_app/index.html")

def register(request):
    valid = User.objects.regValidator(request.POST)

    if valid[0]:
        name = valid[1].name
        messages.add_message(request, messages.SUCCESS, "Thank you for registering " + name + "!")
        return redirect('/')
    else:
        for error in valid[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')

def login(request):
    valid = User.objects.loginValidator(request.POST)

    if valid[0]:
        request.session['name'] = valid[1].name
        request.session['id'] = valid[1].id
        return redirect('/my_page')
    else:
        for error in valid[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect("/")
