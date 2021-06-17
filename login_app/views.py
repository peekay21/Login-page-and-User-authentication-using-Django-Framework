from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def loginpage(request):
     return HttpResponse('loginpage')

def loginauth(request):
     return HttpResponse('loginauth')

def logout(request):
     return HttpResponse('logout')