from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Index(Request):
    return HttpResponse("This is Index Page")