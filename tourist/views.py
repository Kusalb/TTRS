from django.http import HttpResponse
from django.shortcuts import render
import overpy  # to import the overpy module
from tourist.overpass import *
from tourist.models import *

# Create your views here.
def index(request):
    api = overpy.Overpass()
    result = api.query(accommodation_query)
    accomodation_name = list()
    accomodation_contact = list()
    accomodation_email = list()
    accomodation_website = list()
    accomodation_opening_hours = list()
    accomodation_category = list()
    accomodation_latitude = list()
    accomodation_longitude = list()

    for node in result.nodes:  # from each node , get the all tags information
        try:
            name = node.tags["name"]
        except:
            name = node.tags["name"] = ''
        accomodation_name.append(name)
        try:
            contact = node.tags["phone"]
        except:
            contact = node.tags["phone"] = ''
        accomodation_contact.append(contact)
        try:
            email = node.tags["email"]
        except:
            email = node.tags["email"] = ''
        accomodation_email.append(email)

        try:
            website = node.tags["website"]
        except:
            website = node.tags["website"] = ''
        accomodation_website.append(website)
        try:
            opening_hours = node.tags["opening_hours"]
        except:
            opening_hours = node.tags["opening_hours"] = ''
        accomodation_opening_hours.append(opening_hours)

        try:
            category = node.tags["tourism"]
        except:
            category = node.tags["tourism"] = ''
        accomodation_category.append(category)

        try:
            latitude = node.lat
        except:
            latitude = node.lat = ''
        accomodation_latitude.append(latitude)

        try:
            longitude = node.lon
        except:
            longitude = node.lon = ''
        accomodation_longitude.append(longitude)
        if(name != ''):
            print(type(name), type(contact), type(email), type(website), type(opening_hours), type(category), type(latitude), type(longitude))
            data = Accomodation.objects.create(name=name, contact=contact, email=email, website=website,
                                               opening_hours=opening_hours, category=category, latitude=float(latitude),
                                               longitude=float(longitude))
            data.save()
    return HttpResponse("done")


def list(request):
    accommodation = Accomodation.objects.all()
    return render(request, 'tourist/home.html', {'accomodation':accommodation})