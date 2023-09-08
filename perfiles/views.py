from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the perfiles index.")

def login(request):
    return HttpResponse("This is the login page.")

def register(request):
    return HttpResponse("This is the register page.")

def logout(request):
    return HttpResponse("This is the logout page.")

def getProfile(request):
    return HttpResponse("This is the getProfile page.")

def updateProfile(request):
    return HttpResponse("This is the updateProfile page.")