"""
URL configuration for rock_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views


urlpatterns = [
    path('', include ('home.urls')),
    path('admin/', admin.site.urls),
    path('perfiles/', include ('perfiles.urls')),
    path('paginas/', include ('paginas.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path ('registro/', views.registro_view, name='registro'),
    path ('mensaje/', views.mensaje_view, name='mensaje'),
]
