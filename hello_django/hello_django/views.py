from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, "about.html", {"greteeng":'hello serg',"mama":"Ira","papa":"vova"})

def home(requst):
    return HttpResponse('This is my home')