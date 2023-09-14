from django.urls import path
from . import views

app_name = 'perfiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('getProfile', views.getProfile, name='getProfile'),
    path('updateProfile', views.updateProfile, name='updateProfile'),
    path('registro/', views.procesar_registro, name='registro'),
    ]