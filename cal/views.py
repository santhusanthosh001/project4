from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def math(request):
    return render(request,"add.html")
def calculate(request):
    i=int(request.GET["t1"])
    j=int(request.GET["t2"])
    ss=request.GET["oper"]
    z=0
    if ss=="add":
        z=i+j
    elif ss=="sub":
        z=i-j
    elif ss=="mul":
        z=i*j
    else:
        z = i/j
    return HttpResponse("the result")

