from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
import overpy  # to import the overpy module
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from tourist.overpass import *
from tourist.models import *


# Create your views here.
def get_tourism_data(request):
    Tourism.objects.all().delete()
    api = overpy.Overpass()
    result = api.query(tourism_query)
    print(result)
    tourism_name = list()
    tourism_contact = list()
    tourism_email = list()
    tourism_address = list()
    tourism_website = list()
    tourism_opening_hours = list()
    tourism_category = list()
    tourism_latitude = list()
    tourism_longitude = list()

    for node in result.nodes:  # from each node , get the all tags information
        try:
            name = node.tags["name"]
        except:
            name = node.tags["name"] = ''
        tourism_name.append(name)
        print(tourism_name)
        try:
            contact = node.tags["phone"]
        except:
            contact = node.tags["phone"] = ''
        tourism_contact.append(contact)
        try:
            email = node.tags["email"]
        except:
            email = node.tags["email"] = ''
        tourism_email.append(email)

        try:
            website = node.tags["website"]
        except:
            website = node.tags["website"] = ''
        tourism_website.append(website)
        try:
            opening_hours = node.tags["opening_hours"]
        except:
            opening_hours = node.tags["opening_hours"] = ''
        tourism_opening_hours.append(opening_hours)

        try:
            category = node.tags["tourism"]
        except:
            category = node.tags["tourism"] = ''
        tourism_category.append(category)
        try:
            address = node.tags["addr:street"]
        except:
            address = node.tags["addr:street"] = ''
        tourism_address.append(address)
        try:
            latitude = node.lat
        except:
            latitude = node.lat = ''
        tourism_latitude.append(latitude)

        try:
            longitude = node.lon
        except:
            longitude = node.lon = ''
        tourism_longitude.append(longitude)
        if (name != ''):
            print(name, contact, email, website, contact, email, website, opening_hours, category, longitude, latitude)
            data = Tourism.objects.create(name=name, contact=contact, email=email, website=website, address=address,
                                          opening_hours=opening_hours, category=category, latitude=float(latitude),
                                          longitude=float(longitude))
            data.save()
    return redirect('admin_dashboard')


def list_tourism_data(request):
    tourism = Tourism.objects.all()
    return render(request, 'tourist/home.html', {'tourism': tourism})


def index(request):
    return render(request, 'tourist/index.html')


def category_filter(request):
    if request.method == "POST":
        category = request.POST['category']
        tourism = Tourism.objects.filter(category=category)
    return render(request, 'tourist/home.html', {'tourism': tourism})


def sign_up(request):
    if request.method == "GET":
        return render(request, 'tourist/registration/sign_up.html')
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        hashed_password = make_password(password)
        role = request.POST["role"]
        try:
            if (role == "is_admin"):
                user_create = CustomUser.objects.create(username=username, password=hashed_password, is_admin=True)
                user_create.save()
            elif (role == "is_user"):
                user_create = CustomUser.objects.create(username=username, password=password, is_user=True)
                user_create.save()
        except:
            return redirect('login')
        return redirect('login')


def login(request):
    if request.method=="GET":
        return render(request, 'tourist/registration/login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_user == 1:
                return redirect('user_dashboard')
            elif user.is_admin == 1:
                return redirect('admin_dashboard')
        else:
            return redirect('login')
    return redirect('login')


def admin_dashboard(request):
    return render(request, 'tourist/registration/admin_dashboard.html')


def user_dashboard(request):
    return render(request, 'tourist/registration/user_dashboard.html')

def signout(request):
    logout(request)
    return redirect('login')