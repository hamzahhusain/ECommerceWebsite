from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
        else:
            messages.error(request,"Incorrect Credentials. Please try again.")
    form = AuthenticationForm()
    context = {'loginForm': form}
    return render(request,'shop/index.html', context)

def test(request):
    return render(request,'shop/index.html')

def shopLogout(request):
    logout(request)
    return render(request,'shop/index.html')