
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    #routes to user dashboard after logging in
    url(r'^add$', views.add),
    #routes to add function in pet_app views
    url(r'^show/(?P<id>\d+)$', views.show),
    #routes to the show/profile page of a certain user
    url(r'^createPet$', views.createPet),
    #comes from the form in add.html to createPet fx in views
    url(r'^destroy/(?P<id>\d+$)', views.destroy)
]
