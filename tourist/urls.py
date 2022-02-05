from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from TTRS import settings
from tourist import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list', views.list, name="list")

]