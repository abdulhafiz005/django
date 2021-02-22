from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("home page")

# def index(request):
#     data = {'name': 'hafiz'}
#     return render(request, 'index.html', data)

def index(request):
    return render(request, "index.html")

def fullname(request):
    fname = request.get.GET('first_name')
    lname = request.get.GET('last_name')
    return HttpResponse(f"{fname} {lname}")