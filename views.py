from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def testing(request):
    print("hello")
    return render(request,"homepage.html")
