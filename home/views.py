from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    context = {
        "latest_question_list": "",
    }
    return render(request, "index.html", context)

def about(request):
    context = {
        "latest_question_list": "",
    }
    return render(request, "about.html", context)

def pages(request):
    context = {
        "latest_question_list": "",
    }
    return render(request, "pages.html", context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('página_principal')
        
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('página_principal')


# Create your views here.
