from django.http import HttpResponse
from django.shortcuts import render

def values(request):
    return render(request, 'values.html')

def sum(request):
    sum = {"sum": (int(request.GET.get('val1')) + int(request.GET.get('val2')))}
    return render(request, 'sum.html', sum)