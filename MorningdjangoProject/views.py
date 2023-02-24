import datetime
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    now=datetime.datetime.now()
    html="<html><body><h2>Now time is %s.</h2></body></html>"%now
    return HttpResponse(html)
def welcome(request):
    return HttpResponse("Welcome to Django class")
def emobilis(request):
    return HttpResponse("eMobilis mobile Technology Institute")
def Home(request):
    return render(request, 'home.html')
def Services(request):
    return render(request, 'Services.html')
def Contacts(request):
    return render(request, 'Contact us.html')
def About(request):
    return render(request, 'About us.html')


