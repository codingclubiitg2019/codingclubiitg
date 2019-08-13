from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'CodingClubIITG/index.html')

def aboutus(request):
    return render(request, 'CodingClubIITG/aboutus.html')

def events(request):
    return render(request, 'CodingClubIITG/blogtwo.html')

def blog(request):
    return render(request, 'CodingClubIITG/blogone.html')

def projects(request):
    return render(request, 'CodingClubIITG/portfolio.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)

                    messages.success(request, f'Your account has been created!')
                    return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'CodingClubIITG/register.html', {'form': form})