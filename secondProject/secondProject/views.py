from django.http import HttpResponse
from django.shortcuts import render

def values(request):
    return render(request, 'values.html')

def sum(request):
    ans = None
    operator = request.GET.get('operator')
    val1 = request.GET.get('val1')
    val2 = request.GET.get('val2')
    if operator == '+':
        ans = {"ans": (int(val1) + int(val2))}
    elif operator == '-':
        ans = {"ans": (int(val1) - int(val2))}
    elif operator == '*':
        ans = {"ans": (int(val1) * int(val2))}
    elif operator == '/':
        ans = {"ans": (int(val1) / int(val2))}
    else:
        ans = {"ans": "something went wrong."}
    return render(request, 'sum.html', ans)