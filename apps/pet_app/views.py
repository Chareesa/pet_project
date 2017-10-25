# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User
from .models import Pet


# Create your views here.
def dashboard(request):
    context = {
        'other_users': User.objects.exclude(id = request.session['id']),
        'petz': Pet.objects.filter(owner_id = request.session['id']),
    }
    return render(request, 'pet_app/dashboard.html', context)

def add(request):
    return render(request, 'pet_app/add.html')

def createPet(request):
    Pet.objects.create(
        pet_name = request.POST['name'],
        pet_type = request.POST['petType'],
        owner = User.objects.get(id= request.session['id'])
    )
    return redirect('/pet/dashboard')
def show(request, id):
    context = {
        'person': User.objects.get(id = id),
        'petz': User.objects.get(id = id).pets_owned.all()
        #uses User.objects.get.pets_owned.all because it's getting all the pets
        #   through the User models related_field
    }
    return render(request, 'pet_app/show.html', context)

def destroy(request, id):
    Pet.objects.get(id=id).delete()
    return redirect('/pet/dashboard')