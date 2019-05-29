from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'CodingClubIITG/index.html')

def aboutus(request):
    return render(request, 'CodingClubIITG/aboutus.html')

def events(request):
    return render(request, 'CodingClubIITG/blogtwo.html')

def blog(request):
    return render(request, 'CodingClubIITG/blogone.html')

def projects(request):
    return render(request, 'CodingClubIITG/portfolio.html')