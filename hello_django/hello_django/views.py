from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, "about.html", {"greteeng":'hello serg',"mama":"Ira","papa":"vova"})

def home(requst):
    return render(requst, "home.html")

def reverse(requst):
    user_text = requst.GET['usertext']
    reverse = user_text[::-1]
    return render(requst, "reverse.html",{'key':reverse})