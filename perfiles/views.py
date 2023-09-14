from profile import Profile
from django.shortcuts import render, redirect
from django.shortcuts import redirect, render
from django.http import HttpResponse

from perfiles.apps import PerfilesConfig

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

def procesar_registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        correo = request.POST['correo']
        genero = request.POST['genero']        
        
        
        return redirect('registro_exitoso')
    
    return render(request, 'home/registro.html')

